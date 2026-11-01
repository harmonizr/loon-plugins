#!/usr/bin/env python3
"""把插件引用的第三方脚本镜像到本仓库 scripts/ 下，并生成 url -> 本地路径 映射。"""
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.request
from collections import Counter
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1"
LOON_UA = "Loon/3.5.2(1005) CFNetwork/3826 Darwin/24.0.0"

# 需要镜像的托管域名
MIRROR_HOSTS = {
    "raw.githubusercontent.com", "loon.103516.xyz", "rucu6.pages.dev",
    "kelee.one", "ddgksf2013.top", "reven.jsforbaby.workers.dev",
    "github.com", "devchristian1337.github.io",
}
SCRIPT_EXT = (".js", ".jq", ".json", ".sgmodule", ".html", ".txt")

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


OWN_REPO = "harmonizr/loon-plugins"


def is_mirrorable(u):
    p = urlparse(u)
    # 绝不镜像本仓库自己的地址（否则每次同步都会自我复制一份）
    if OWN_REPO in p.path:
        return False
    if p.netloc not in MIRROR_HOSTS:
        return False
    if "${" in u or "$1" in u:
        return False
    path = p.path.lower()
    if re.search(r"\.(png|jpe?g|gif|webp|ico|svg)$", path):
        return False
    # github.com 只镜像 release 里的 bundle 之类
    if p.netloc == "github.com" and "/releases/" not in path:
        return False
    return True


def local_name(u):
    p = urlparse(u)
    host = p.netloc
    if host == "raw.githubusercontent.com":
        parts = [x for x in p.path.strip("/").split("/") if x]
        if len(parts) >= 2 and parts[2:3] == ["refs"]:
            repo = f"{parts[0]}__{parts[1]}"
            rest = parts[4:]
        else:
            repo = f"{parts[0]}__{parts[1]}"
            rest = parts[2:]
        sub = "/".join(rest[:-1]) if len(rest) > 1 else ""
        name = rest[-1] if rest else "index"
        rel = f"{host}/{repo}/{sub}".rstrip("/") + "/" + name
    elif host == "github.com":
        rel = host + p.path.strip("/")
    else:
        rel = host + p.path.rstrip("/")
    rel = re.sub(r"[^\w./\-@]", "_", rel)
    if not os.path.splitext(rel)[1] and not rel.endswith(".js"):
        rel += ".js"
    return "scripts/" + rel


def resolve_conflicts(mapping_all):
    """同一父目录下，某文件已存在为目录 / 某目录已存在为文件时，重命名条目。"""
    for u, rel in list(mapping_all.items()):
        dest = os.path.join(HERE, rel)
        if os.path.exists(dest) and os.path.isdir(dest):
            mapping_all[u] = rel + ".index.js"
        elif os.path.exists(dest) and not os.path.isfile(dest):
            mapping_all[u] = rel + ".bak"
    return mapping_all


def fetch(u, retries=4):
    last = None
    for i in range(retries):
        ua = LOON_UA
        req = urllib.request.Request(u, headers={"User-Agent": ua, "Accept": "*/*",
                                                 "Accept-Encoding": "identity"})
        try:
            with urllib.request.urlopen(req, timeout=45, context=ctx) as r:
                data = r.read()
                if r.status == 200 and data:
                    return data
                last = f"HTTP {r.status}"
        except Exception as e:  # noqa: BLE001
            last = repr(e)
        time.sleep(1.2 * (i + 1))
    raise RuntimeError(f"{u}: {last}")


def main():
    refs = json.load(open(sys.argv[1]))
    targets = sorted(u for u in refs if is_mirrorable(u))
    print(f"待镜像 {len(targets)} 个 URL")
    os.makedirs(os.path.join(HERE, "scripts"), exist_ok=True)
    mapping, failed = {}, []
    for i, u in enumerate(targets, 1):
        rel = local_name(u)
        dest = os.path.join(HERE, rel)
        if os.path.isdir(dest):
            rel += ".index.js"
            dest = os.path.join(HERE, rel)
        try:
            if os.path.exists(dest) and os.path.getsize(dest) > 0:
                data = open(dest, "rb").read()
            else:
                data = fetch(u)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "wb").write(data)
            mapping[u] = {"path": rel, "bytes": len(data),
                          "sha256": hashlib.sha256(data).hexdigest()}
        except Exception as e:  # noqa: BLE001
            print("  FAIL", u[:90], e)
            failed.append(u)
        if i % 25 == 0 or i == len(targets):
            print(f"  [{i}/{len(targets)}] ok={len(mapping)} fail={len(failed)}", flush=True)
        time.sleep(0.2)
    json.dump(mapping, open(os.path.join(HERE, "scripts-mapping.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"完成：成功 {len(mapping)}，失败 {len(failed)}")
    if failed:
        print("失败列表:")
        for f in failed:
            print("  ", f)


if __name__ == "__main__":
    main()

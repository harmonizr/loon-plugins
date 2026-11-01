#!/usr/bin/env python3
"""
同步 loonlab.103516.xyz 的 Loon 插件到本仓库。

用法:
    python3 sync.py            # 增量同步（默认）
    python3 sync.py --force    # 全量重下
    python3 sync.py --check    # 只检查上游是否有更新，不写入

要点:
    源站 loon.103516.xyz 对普通浏览器/curl 会把请求 302 跳到 Telegram，
    只认 Loon 客户端的 UA（Loon/x.x.x CFNetwork/...），脚本已带上。
"""
import hashlib
import json
import os
import random
import ssl
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX_URLS = {
    "plugins.all.json": "https://loonlab.103516.xyz/Plugin/plugins.all.json",
    "plugins.json": "https://loonlab.103516.xyz/Plugin/plugins.json",
}
PLUGIN_URL = "https://loon.103516.xyz/Plugin/{}"
REFERER = "https://loonlab.103516.xyz/Plugin/"
UA = "Loon/3.5.2(1005) CFNetwork/3826 Darwin/24.0.0"

_ctx = ssl.create_default_context()
_ctx.check_hostname = False
_ctx.verify_mode = ssl.CERT_NONE


def http_get(url, retries=4, referer=REFERER):
    """带重试的 GET，返回 bytes。"""
    last = None
    for i in range(retries):
        headers = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "identity"}
        if referer:
            headers["Referer"] = referer
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=headers), timeout=40, context=_ctx
            ) as r:
                data = r.read()
                if r.status == 200 and data:
                    return data
                last = "HTTP %s" % r.status
        except Exception as e:  # noqa: BLE001
            last = repr(e)
        time.sleep(1.5 * (i + 1) + random.random())
    raise RuntimeError("%s: %s" % (url, last))


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def main():
    force = "--force" in sys.argv
    check_only = "--check" in sys.argv

    # 1. 拿上游索引
    indexes = {}
    for name, url in INDEX_URLS.items():
        raw = http_get(url)
        indexes[name] = raw
        if not check_only:
            open(os.path.join(HERE, name), "wb").write(raw)
    all_meta = json.loads(indexes["plugins.all.json"])
    plugins = all_meta.get("plugins", [])

    # 2. 合并本地清单里已有的 sha256，便于判断变化
    manifest_path = os.path.join(HERE, "manifest.json")
    old = {}
    if os.path.exists(manifest_path):
        try:
            for p in json.load(open(manifest_path))["plugins"]:
                old[p.get("filename")] = p.get("sha256")
        except Exception:  # noqa: BLE001
            pass

    out_dir = os.path.join(HERE, "plugins")
    os.makedirs(out_dir, exist_ok=True)

    print("上游索引更新于 %s，共 %d 个插件" % (all_meta.get("last_updated"), len(plugins)))

    added, updated, same, failed, manifest = [], [], [], [], []
    for i, p in enumerate(plugins, 1):
        fn = p.get("filename") or os.path.basename(p["url"])
        dest = os.path.join(out_dir, fn)
        entry = dict(p)
        entry["local_path"] = "plugins/" + fn
        try:
            need = force or not os.path.exists(dest)
            if need:
                body = http_get(p.get("url") or PLUGIN_URL.format(fn))
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "wb").write(body)
            else:
                body = open(dest, "rb").read()
            digest = sha256(body)
            prev = old.get(fn)
            if need:
                (added if prev is None else updated).append(fn)
            elif prev and prev != digest:
                updated.append(fn)
            else:
                same.append(fn)
            if not body.startswith(b"#!name"):
                print("  ! %s 不是 Loon 插件格式（可能被反爬页替换）" % fn)
            entry["bytes"] = len(body)
            entry["sha256"] = digest
        except Exception as e:  # noqa: BLE001
            print("  FAIL %s: %s" % (fn, e))
            entry["error"] = str(e)
            failed.append(fn)
        manifest.append(entry)
        if i % 20 == 0 or i == len(plugins):
            print("  [%d/%d] 新增 %d / 更新 %d / 未变 %d / 失败 %d"
                  % (i, len(plugins), len(added), len(updated), len(same), len(failed)), flush=True)
        if need:
            time.sleep(0.25)

    if check_only:
        print("check 模式：上游有变化 -> %s" % (bool(added or updated or failed)))
        return

    manifest.sort(key=lambda x: x.get("filename", "").lower())
    json.dump(
        {
            "source": "https://loonlab.103516.xyz/Plugin/",
            "last_updated": all_meta.get("last_updated"),
            "synced_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "count": len(manifest),
            "plugins": manifest,
        },
        open(manifest_path, "w"),
        ensure_ascii=False,
        indent=2,
    )
    print("完成：新增 %s，更新 %s，未变 %d，失败 %d"
          % (added or "无", updated or "无", len(same), len(failed)))
    if failed:
        print("失败列表:", failed)
        sys.exit(1)


if __name__ == "__main__":
    main()

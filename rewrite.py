#!/usr/bin/env python3
"""把 plugins/*.lpx 里所有第三方脚本 URL 重写为本仓库的 raw 地址。

幂等：已改过的插件再跑一次不会产生任何变化（不会自我嵌套）。

用法: python3 rewrite.py --dry      # 只看会改什么
      python3 rewrite.py            # 实际改写
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = "https://raw.githubusercontent.com/harmonizr/loon-plugins/main/"
OWN = "raw.githubusercontent.com/harmonizr/loon-plugins/main/"

mapping = json.load(open(os.path.join(HERE, "scripts-mapping.json")))

# 只匹配「看起来是脚本文件」的 URL，避免 https://域名/ 这类首页地址被误替换
SCRIPT_RE = re.compile(r"\.(js|jq|json|bundle|sgmodule|conf|txt|html)(?=$|[?#\s\"'`,)])", re.I)
url_map = {}
for u, v in mapping.items():
    if not SCRIPT_RE.search(u):
        continue
    if u.endswith("/"):
        continue
    url_map[u] = RAW + v["path"]

keys = sorted(url_map, key=len, reverse=True)

DRY = "--dry" in sys.argv


def rewrite_text(text, stats):
    # 先把已有的自家链接还原成源地址，保证幂等（防止二次改写自我嵌套）
    for u, new in url_map.items():
        if new in text:
            text = text.replace(new, u)
    for u in keys:
        if u in text:
            text = text.replace(u, url_map[u])
            stats[u] = stats.get(u, 0) + 1
    return text


def main():
    _ = OWN  # 保留常量，便于排查
    total = changed = 0
    stats = {}
    for fn in sorted(os.listdir(os.path.join(HERE, "plugins"))):
        if not fn.endswith(".lpx"):
            continue
        path = os.path.join(HERE, "plugins", fn)
        original = open(path, encoding="utf-8", errors="surrogateescape").read()
        new = rewrite_text(original, stats)
        total += 1
        if new != original:
            changed += 1
            if not DRY:
                open(path, "w", encoding="utf-8", errors="surrogateescape").write(new)
    print(f"共 {total} 个插件，改动 {changed} 个，引用 {len(url_map)} 个上游 URL")


if __name__ == "__main__":
    main()

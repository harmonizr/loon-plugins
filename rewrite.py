#!/usr/bin/env python3
"""把 plugins/*.lpx 里所有第三方脚本 URL 重写为本仓库的 raw 地址。

用法: python3 rewrite.py --dry      # 只看会改什么
      python3 rewrite.py            # 实际改写
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = "https://raw.githubusercontent.com/harmonizr/loon-plugins/main/"

mapping = json.load(open(os.path.join(HERE, "scripts-mapping.json")))
url_map = {u: RAW + v["path"] for u, v in mapping.items()}
# 按长度降序，避免短 URL 抢先匹配长 URL 的前缀
keys = sorted(url_map, key=len, reverse=True)

DRY = "--dry" in sys.argv


def rewrite_line(line, stats):
    for u in keys:
        if u in line:
            line = line.replace(u, url_map[u])
            stats[u] = stats.get(u, 0) + 1
    return line


def main():
    total_files = changed = 0
    stats = {}
    for fn in sorted(os.listdir(os.path.join(HERE, "plugins"))):
        if not fn.endswith(".lpx"):
            continue
        path = os.path.join(HERE, "plugins", fn)
        original = open(path, encoding="utf-8", errors="surrogateescape").read()
        before = dict(stats)
        lines = [rewrite_line(line, stats) for line in original.splitlines(keepends=True)]
        new = "".join(lines)
        total_files += 1
        if new != original:
            changed += 1
            delta = {k: stats.get(k, 0) - before.get(k, 0) for k in stats}
            n = sum(v for v in delta.values())
            print(f"  {fn}: 替换 {n} 处")
            if not DRY:
                open(path, "w", encoding="utf-8", errors="surrogateescape").write(new)
    print(f"\n共 {total_files} 个插件，改动 {changed} 个，替换 URL 次数合计 {sum(stats.values())}")
    print(f"涉及不同上游 URL {len(stats)} 个")


if __name__ == "__main__":
    main()

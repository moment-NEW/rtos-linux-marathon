#!/usr/bin/env python3
"""Generate a new weekly log from the docs/logs/weekly-log-YYYY-WW.md template."""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import date, datetime, timedelta
from pathlib import Path
import sys

TEMPLATE_PATH = Path("docs/logs/weekly-log-YYYY-WW.md")
DEFAULT_TEMPLATE = """# 周报模板（替换 YYYY-WW）

- 周次：YYYY-WW
- 时间范围：YYYY-MM-DD ~ YYYY-MM-DD
- 本周重点（3+1 模式中的本周定位）：
- 本周完成：
  - 代码/补丁/PR：
  - 实验/数据：
  - 阅读/学习：
- 遇到的问题 & 解决进展：
- 下周计划：
- 需要协助/决策：
- 备注（链接/日志/截图）：
"""


def parse_week(value: str) -> tuple[int, int]:
    value = value.strip().upper()
    if value.startswith("W"):
        value = value[1:]
    if "-" in value:
        year_str, week_str = value.split("-", 1)
    elif value.startswith("20") and len(value) >= 6:
        year_str, week_str = value[:4], value[4:]
    else:
        raise ValueError(f"无法解析周次: {value}")
    return int(year_str), int(week_str)


def to_week(date_obj: date) -> tuple[int, int]:
    iso = date_obj.isocalendar()
    return iso.year, iso.week


def week_range(year: int, week: int, start_day: int = 1) -> tuple[date, date]:
    try:
        start = date.fromisocalendar(year, week, start_day)
    except ValueError as exc:
        raise ValueError(f"无效的 ISO 年周: {year}-{week}") from exc
    return start, start + timedelta(days=6)


def build_content(template: str, year: int, week: int, start: date, end: date) -> str:
    content = template.replace("YYYY-WW", f"{year:04d}-{week:02d}")
    content = content.replace("YYYY-MM-DD ~ YYYY-MM-DD", f"{start:%Y-%m-%d} ~ {end:%Y-%m-%d}")
    return content


def main() -> int:
    parser = ArgumentParser(description="生成 docs/logs 新周报模板文件")
    parser.add_argument("week", nargs="?", help="目标周次，例如 2026-16 或 2026-W16。默认使用当前日期对应的周次。")
    parser.add_argument("--date", help="使用指定日期生成对应周（格式 YYYY-MM-DD）。")
    parser.add_argument("--week-start", choices=["mon", "wed"], default="mon",
                        help="设置周起始日，mon=周一(默认)、wed=周三。")
    parser.add_argument("--force", action="store_true", help="如果目标文件已存在，则覆盖它。")
    args = parser.parse_args()

    if args.date and args.week:
        parser.error("不能同时指定 --date 和 week 参数。")

    if args.date:
        try:
            target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            parser.error("日期格式必须为 YYYY-MM-DD")
        year, week = to_week(target_date)
    elif args.week:
        try:
            year, week = parse_week(args.week)
        except ValueError as exc:
            parser.error(str(exc))
    else:
        year, week = to_week(date.today())

    start_day = 1 if args.week_start == "mon" else 3
    start, end = week_range(year, week, start_day)
    target = Path("docs/logs") / f"weekly-log-{year:04d}-{week:02d}.md"
    if target.exists() and not args.force:
        print(f"文件已存在: {target}")
        print("如需覆盖，请加上 --force")
        return 1

    template_text = TEMPLATE_PATH.read_text(encoding="utf-8") if TEMPLATE_PATH.exists() else DEFAULT_TEMPLATE
    content = build_content(template_text, year, week, start, end)

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")

    print(f"已生成：{target}")
    print(f"周次：{year:04d}-{week:02d}，时间范围：{start:%Y-%m-%d} ~ {end:%Y-%m-%d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

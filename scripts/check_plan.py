#!/usr/bin/env python3
"""Check a set of modules for time clashes, date by date.

Usage:
    python scripts/check_plan.py WIHN0033 MGTHN0130 MGTHN0112
    python scripts/check_plan.py WIHN0033 MGTHN0130 --busy busy.json --data data/modules.json
    python scripts/check_plan.py MGTHN0112 WIHN0033 --skip "MGTHN0112:Mo 16:15"   # you pick the other exercise group

busy.json lists your fixed commitments (job, teaching, sports):
    [{"date": "2026-11-05", "start": "08:00", "end": "12:15", "label": "Job"},
     {"weekday": "Th", "start": "08:00", "end": "12:00", "label": "No Thursday mornings"}]
"""

import argparse
import json
from collections import Counter


def appointments(modules, code, skip):
    if code not in modules:
        raise SystemExit(f"{code} is not in the data file. Fetch it first: python scripts/tumonline.py fetch ...")
    return [dict(a, label=code) for part in modules[code]["parts"] for a in part["appointments"]
            if f'{code}:{a["weekday"]} {a["start"]}' not in skip]


def overlaps(a, b):
    return a["start"] < b["end"] and b["start"] < a["end"]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("codes", nargs="+")
    p.add_argument("--data", default="data/modules.json")
    p.add_argument("--busy", help="JSON file with your fixed commitments")
    p.add_argument("--skip", action="append", default=[],
                   help='drop a weekly slot you will not attend, e.g. "MGTHN0112:Mo 16:15" (repeatable)')
    a = p.parse_args()

    with open(a.data) as f:
        modules = json.load(f)["modules"]
    plan = [x for code in a.codes for x in appointments(modules, code, set(a.skip))]
    busy = json.load(open(a.busy)) if a.busy else []

    clashes = set()
    for i, x in enumerate(plan):
        for y in plan[i + 1:]:
            if x["date"] == y["date"] and x["label"] != y["label"] and overlaps(x, y):
                clashes.add((x["date"], x["weekday"], f'{x["label"]} {x["start"]}-{x["end"]}',
                             f'{y["label"]} {y["start"]}-{y["end"]}'))
        for b in busy:
            same_day = b.get("date") == x["date"] or b.get("weekday") == x["weekday"]
            if same_day and overlaps(x, b):
                clashes.add((x["date"], x["weekday"], f'{x["label"]} {x["start"]}-{x["end"]}',
                             f'{b["label"]} {b["start"]}-{b["end"]}'))

    days = Counter(x["weekday"] for x in plan)
    print(f"{len(plan)} dates. Days with classes (count of dates): {dict(days)}")
    if not clashes:
        print("No clashes.")
    for c in sorted(clashes):
        print(f"CLASH {c[0]} ({c[1]}): {c[2]}  <->  {c[3]}")


if __name__ == "__main__":
    main()

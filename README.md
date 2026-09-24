# coursepilot

Plan your TUM semester with Claude. For every TUM student, any program, any campus: drop in your module plan, name your campus, and let Claude build the timetable.

coursepilot connects [Claude Code](https://claude.com/claude-code) to TUMonline with your personal API token. Claude looks up every course of your program in a semester (dates, rooms, lecturers, exam format, content), checks them against your module plan and your progress, and proposes a clash-free timetable. You stop clicking through TUMonline tab by tab.

Shared by **hn.ai**, the place in Heilbronn where students show each other the AI workflows they use for their studies.

## How it works

1. **Your module plan** (Modulhandbuch / study plan PDF) goes into `data/`. It tells Claude which modules count for what.
2. **Your profile** (`my-profile.md`) tells Claude your campus, what you passed, what you still need and how you like to study.
3. **TUMonline** tells Claude what actually runs this semester, when and where.
4. You type `/plan-semester`. Claude combines all three and answers with a weekly timetable, ECTS per category, exam formats, clashes and deadlines.

## What you can ask

> "I still need 10 ECTS in my elective catalog. No written exams, and keep Fridays free. What fits?"

> "What is the exam format of IN2346, and who teaches it this winter?"

> "Does this seminar clash with anything in my plan?"

## Quick start

1. **Get your TUMonline token** (5 minutes): [docs/1-get-your-token.md](docs/1-get-your-token.md)
2. **Set up Claude Code and this repo**: [docs/2-connect-claude.md](docs/2-connect-claude.md)
3. **Add your module plan, campus and progress**: [docs/3-add-your-study-plan.md](docs/3-add-your-study-plan.md)
4. Open a terminal in this folder, run `claude` and type `/plan-semester`.

## What is in here

| File | What it does |
|---|---|
| `tumonline.py` | Talks to TUMonline: token check, course search (with campus sorting), all courses of a module, full course details |
| `check_plan.py` | Checks a set of modules for clashes, date by date, including your own fixed commitments |
| `CLAUDE.md` | Tells Claude how to use the tools and which TUMonline pitfalls to avoid |
| `.claude/commands/plan-semester.md` | The `/plan-semester` workflow |
| `my-profile.example.md` | Template for your campus, progress and preferences |
| `data/` | Your module plan PDF and downloaded course data (ignored by git) |

Both scripts use only the Python standard library. No `pip install` needed.

## Works for all campuses

coursepilot finds courses through the **module codes** in your module plan (like `IN2346`, `MGTHN0112`, `WZ1234`). Module codes are unique across TUM, so this works the same in Munich, Garching, Freising/Weihenstephan, Straubing, Heilbronn and online.

The free-text search can sort results by campus (`--campus Heilbronn`). TUMonline has no campus field, so this uses chair names and is a hint, not a filter.

## Privacy

- Your token is a personal credential. It lives in `.env`, which git ignores. Never share or commit it.
- Grant the token only the rights it needs (course information). You can revoke it any time in TUMonline.
- Your profile and your module plan stay in `my-profile.md` and `data/`, both ignored by git.
- Claude reads these files locally. Nothing gets published.

## Limits

- TUMonline publishes exam dates late, usually weeks into the semester. coursepilot shows the exam *format* early. The dates follow later.
- TUMonline often leaves the exam format empty. Claude then reads it from your module plan.
- A module in your plan might not run this semester, and a course outside your plan needs a recognition (Anerkennung) before it counts. Claude flags both, but your examination board decides.
- Always double-check before you register. Registration windows and seminar applications stay your job.

## Contributing

Found a TUMonline quirk, or a tip for your program or campus? Open an issue or a pull request.

License: MIT

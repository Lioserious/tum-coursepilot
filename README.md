# tum-coursepilot

Plan your TUM semester with Claude. For every TUM student, any program, any campus: drop in your module plan, name your campus, and let Claude build the timetable.

coursepilot connects [Claude Code](https://claude.com/claude-code) to TUMonline with your personal API token. Claude looks up every course of your program in a semester (dates, rooms, lecturers, exam format, content), checks them against your module plan and your progress, and proposes a clash-free timetable. You stop clicking through TUMonline tab by tab.

Shared by **hn.ai**, the place in Heilbronn where students show each other the AI workflows they use for their studies.

> **Unofficial community project.** tum-coursepilot is built by students of hn.ai. It is not affiliated with, endorsed by or supported by the Technical University of Munich (TUM). "TUM" and "TUMonline" refer to the university and its systems only to describe what this tool works with. For official information, always check TUMonline and your school.

## How it works

1. **Your module plan** (Modulhandbuch / study plan PDF) goes into `data/`. It tells Claude which modules count for what.
2. **Your profile** (`my-profile.md`) tells Claude your campus, what you passed, what you still need and how you like to study.
3. **TUMonline** tells Claude what actually runs this semester, when and where.
4. You type `/plan-semester` (or `/start` the first time). Claude combines all three and answers with a weekly timetable, ECTS per category, exam formats, clashes and deadlines.

## What you can ask

> "I still need 10 ECTS in my elective catalog. No written exams, and keep Fridays free. What fits?"

> "What is the exam format of IN2346, and who teaches it this winter?"

> "Does this seminar clash with anything in my plan?"

## Before you start

You need three tools. No Python packages, the scripts use only the standard library.

| Tool | Why | Check |
|---|---|---|
| [Claude Code](https://code.claude.com/docs/en/setup) (paid Claude plan) | runs the guide and does the planning | `claude --version` |
| Python 3.8+ | runs the TUMonline scripts | `python3 --version` (Windows: `py --version`) |
| Git (optional) | downloads the repo and updates | `git --version` |

Something missing? **[docs/0-install.md](docs/0-install.md)** has the install command for macOS, Windows and Linux. Once Claude Code runs, `/start` checks Python and Git for you and tells you exactly what to install.

## Quick start

```bash
git clone https://github.com/Lioserious/tum-coursepilot.git
cd tum-coursepilot
claude
```

Then type **`/start`**. The guide walks you through everything, one step at a time, and asks the right questions:

1. **Token:** gets your personal TUMonline token set up and tested (about 5 minutes)
2. **Module plan:** tells you where to find your Modulhandbuch and transcript, and reads them
3. **Profile:** asks about your campus, progress, exam preferences, free days and key dates
4. **Plan:** hands you over to `/plan-semester` for your timetable

Prefer to read first? The guide follows these docs:
[0. Install](docs/0-install.md) · [1. Token](docs/1-get-your-token.md) · [2. Claude Code](docs/2-connect-claude.md) · [3. Module plan and profile](docs/3-add-your-study-plan.md)

## What is in here

| File | What it does |
|---|---|
| `scripts/tumonline.py` | Talks to TUMonline: token check, course search (with campus sorting), all courses of a module, full course details |
| `scripts/check_plan.py` | Checks a set of modules for clashes, date by date, including your own fixed commitments |
| `CLAUDE.md` | Tells Claude how to use the tools and which TUMonline pitfalls to avoid |
| `.claude/skills/coursepilot-guide/` | The setup guide behind `/start`: asks questions, checks every step |
| `.claude/commands/start.md` | `/start`, guided setup |
| `.claude/commands/plan-semester.md` | `/plan-semester`, the planning workflow |
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

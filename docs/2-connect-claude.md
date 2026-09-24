# 2. Connect Claude

This guide sets up Claude Code in the coursepilot folder, so Claude can use your token and the planning tools.

## What you need

- Python 3.8 or newer (`python3 --version`)
- Git
- A Claude account with access to Claude Code. The [Claude Code page](https://claude.com/claude-code) has the current install instructions.

## Step 1: Get the repo

```bash
git clone <this repo's URL> coursepilot
cd coursepilot
```

## Step 2: Add your token

Follow [1-get-your-token.md](1-get-your-token.md) if you have not yet. Then check:

```bash
python3 tumonline.py status
```

## Step 3: Start Claude in this folder

```bash
claude
```

Claude Code reads `CLAUDE.md` automatically. That file explains the tools, the TUMonline pitfalls and the rules, for example never to print your token.

When Claude runs a script for the first time, Claude Code asks for your permission. Allow `python3 tumonline.py` and `python3 check_plan.py`.

## Step 4: Try it

```
/plan-semester
```

Or just ask:

- "Search TUMonline for machine learning courses in Heilbronn this winter."
- "Show me the dates, lecturers and exam format of module WIHN0033."
- "Do MGTHN0112 and WIHN0033 clash?"

## Optional: let Claude see your calendar

If you connect Google Calendar to Claude (claude.ai → Settings → Connectors), Claude can read your fixed commitments (job, teaching, sports) and plan around them. Without it, list your commitments in `my-profile.md`.

## Useful commands (you or Claude can run them)

```bash
python3 tumonline.py search "Process Mining" --semester 26W   # free-text search
python3 tumonline.py module CITHN2004 --semester 26W          # all courses of a module, with dates
python3 tumonline.py course 950945134                         # one course by its TUMonline id
python3 tumonline.py fetch my-modules.txt --semester 26W      # many modules into data/modules.json
python3 check_plan.py WIHN0033 MGTHN0130 --busy busy.json     # clash check
```

Semester ids: `26W` = winter 2026/27, `27S` = summer 2027.

---
description: Build a clash-free semester plan from TUMonline, your handbook and your profile
---

Plan the student's next semester. Follow CLAUDE.md.

1. Run `python3 tumonline.py status`. On an error, stop and walk the student through `docs/1-get-your-token.md`.
2. Read `my-profile.md` and the module plan in `data/`. If something essential is missing (campus, program, semester, passed modules, open ECTS per category, constraints), ask for it in one consolidated question and save the answers to `my-profile.md`. Without a module plan in `data/`, ask the student to add one first.
3. From the module plan, list the candidate modules for every category that still needs ECTS. Filter by the student's interests and exam preferences.
4. Write the candidates to `data/candidates.txt`, one `CODE  # Module name` per line, and run `python3 tumonline.py fetch data/candidates.txt --semester <id>`.
5. Drop candidates without dates. Read the exam format from the module plan where TUMonline leaves it empty.
6. Put the student's fixed commitments into `data/busy.json`, then test combinations with `python3 check_plan.py`. Prefer: no clashes, the student's exam preference, fewer days on campus, their interests.
7. Answer as described in CLAUDE.md under "What a good answer contains". Recommend one plan, give at most two alternatives.
8. Offer next steps: registration and application deadlines, emails to chairs (as drafts), calendar entries.

$ARGUMENTS

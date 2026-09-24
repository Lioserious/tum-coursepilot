# tum-coursepilot

Instructions for Claude: help any TUM student (any program, any campus) pick courses and build a clash-free timetable from live TUMonline data.

## First contact

If `.env` has no token, `data/` has no module plan, or `my-profile.md` is missing, offer the guided setup (`/start`, skill `coursepilot-guide`) before anything else.

## Sources, in this order

1. `my-profile.md`: the student's campus, program, progress, preferences and blocked dates. If it is missing, ask for the essentials in one question (campus, program, what they passed, what they still need, constraints) and write `my-profile.md` from `my-profile.example.md`.
2. `data/*.pdf`: the module plan (Modulhandbuch, study plan, FPSO). It is the authority on which module counts for which category, ECTS, and exam format. If `data/` holds no module plan, ask the student to add one (see `docs/3-add-your-study-plan.md`) before you recommend modules.
3. TUMonline via `tumonline.py`: what actually runs this semester, when, where, and who teaches it.

## Tools

```bash
python3 tumonline.py status                          # token check
python3 tumonline.py search "<text>" --semester 26W [--campus Garching]  # fuzzy, campus matches first (*)
python3 tumonline.py module <CODE> [--name "<module name>"] --semester 26W  # all courses of a module: dates, lecturers, exam mode
python3 tumonline.py course <ID>                     # one course by TUMonline id
python3 tumonline.py fetch <codes.txt> --semester 26W --out data/modules.json
python3 check_plan.py <CODE> <CODE> ... [--busy busy.json] [--skip "CODE:Mo 16:15"]
```

Semester ids: `26W` = winter 2026/27, `27S` = summer 2027.

## Rules

- **Never print, echo or paste the token.** Do not `cat .env`. The scripts read it themselves.
- **Never request a token yourself and never guess a TUM ID.** Send the student to `docs/1-get-your-token.md`. A token requested with a wrong ID lands on a stranger's account.
- If a script reports a token error, explain it with the troubleshooting table in `docs/1-get-your-token.md`.
- Do not register the student for anything and do not send emails. Draft, then let them act.

## Campus

- Module codes are unique across TUM. Find courses by the codes from the module plan and the campus takes care of itself.
- TUMonline has no campus field. `--campus` only sorts by chair name. Heilbronn and Straubing chairs often name their campus, Munich and Garching chairs rarely do. Before recommending a search hit, check its rooms (`course <ID>`) or chair against the student's campus.
- Students with courses on two campuses need travel time between them. Flag back-to-back slots on different campuses.

## TUMonline pitfalls

- **Search is fuzzy.** A name search returns courses from every campus and program. Use `module <CODE>`: it keeps only courses with the exact module code in their title. When you search by name, check the chair and room before trusting a hit.
- **Some courses omit the code in their title.** Always pass the module name too (`--name`, or `CODE  # Name` lines for `fetch`). Results marked `"matched_by": "name"` are a best guess: check chair and campus before you use them.
- **One module has several courses.** Lecture (VO), exercise (UE) and seminar (SE) are separate entries. `module` collects them all. Look at all of them before calling a slot free.
- **Alternative groups.** Some exercises run in parallel groups. The student attends one. Use `--skip` in `check_plan.py` for the group they will not take.
- **"Fach" (FA) entries without dates** mean the module exists but is not scheduled (yet). Report it as "no dates", not as "free".
- **Exam format is often empty** in TUMonline. Read it from the handbook ("Beschreibung der Studien-/Prüfungsleistungen").
- **Exam dates come late.** TUMonline publishes them weeks into the semester. Say "not published yet" instead of guessing, and give the lecture period end as the earliest likely exam time.
- **Block courses** show only a few dates. Check the handbook for coursework after the block (term paper, later presentation) before calling the course "done early".
- **Handbook ≠ offer.** The handbook says when a module usually runs. Only TUMonline says whether it runs this semester.
- **Outside the handbook = recognition needed.** Courses from other schools can count only after the examination board approves them (Anerkennung). Flag that every time.
- **Seminars often need a separate application** (Moodle, matching system, email) with an early deadline. Tell the student to check.

## What a good answer contains

1. A weekly grid (days × time slots) of the proposed plan.
2. ECTS per category: required, done, planned, still open.
3. Per module: category, ECTS, slot, lecturer, exam format, when it is due.
4. Clashes with other courses and with the student's commitments, date by date, from `check_plan.py`.
5. Open questions and deadlines: applications, recognitions, missing exam dates.

Lead with the recommendation. Keep alternatives short. If the student's constraints conflict, say which one breaks and ask.

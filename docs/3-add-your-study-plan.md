# 3. Add your module plan, campus and progress

This guide gives Claude the things TUMonline cannot tell it: your program's rules, your campus and your own progress. It works for every TUM program.

## Step 1: Add your module plan

Every TUM program publishes a module handbook (Modulhandbuch) or study plan as a PDF. It lists which modules count for which category, how many ECTS they give, when they usually run and how they get examined.

Where to find it:

- **TUMonline:** open your program's curriculum (Studienplan / curriculum support). Most programs link the module handbook there.
- **Your school's website:** search for "<your program> Modulhandbuch" or "module handbook".
- **Study plan or FPSO:** if your program has a separate document with the required ECTS per category, add it too.

Save the files into `data/`, for example:

```
data/modulhandbuch.pdf
data/fpso.pdf
```

Claude reads PDFs directly. The handbook often knows the exam format when TUMonline leaves it empty.

## Step 2: Fill in your profile

```bash
cp my-profile.example.md my-profile.md
```

Fill in:

- **campus**: Munich, Garching, Freising/Weihenstephan, Straubing, Heilbronn, or several
- program, degree and the semester you plan for
- the ECTS your program requires per category
- the modules you already passed, and in which category they count
- your preferences: exams or projects, free days, fixed commitments, interests
- key dates: semester abroad, internship, anything that blocks the exam period

No time? Leave it empty. `/plan-semester` asks for the essentials and fills the file for you.

The more honest this file, the better the plan. Git ignores `my-profile.md`, so it stays on your machine.

## Step 3: Plan

Start `claude` in the folder and run `/plan-semester`. Claude reads your profile and module plan, asks what is missing, pulls the courses from TUMonline and proposes a timetable.

Check the result before you register. Claude works from TUMonline and your module plan, and both can be out of date. Registration windows, seminar applications and recognitions stay your job.

# 1. Get your TUMonline token

This guide gets you a personal TUMonline API token in about 5 minutes. You need it once. Claude uses it to read the course catalog for you.

## What the token is

TUMonline has a web service (`wbservicesbasic`) that returns course data. It only answers requests that carry a token, and that token belongs to you. You request it with your TUM ID, activate it in TUMonline, and decide what it may read.

## Step 1: Request the token

Open this URL in your browser. Replace `YOUR_TUM_ID` with **your own** TUM ID (the short one, like `ab12cde`):

```
https://campus.tum.de/tumonline/wbservicesbasic.requestToken?pUsername=YOUR_TUM_ID&pTokenName=coursepilot
```

TUMonline answers with a short XML document:

```xml
<token>32 letters and digits</token>
```

Copy the 32 characters between the tags.

> **Type your TUM ID yourself.** Do not let an AI assistant guess it from files on your computer. If it picks a wrong ID, the token lands on someone else's account and that person gets the activation email.

If you prefer the terminal, this saves the answer to a file instead of showing it:

```bash
curl -sS "https://campus.tum.de/tumonline/wbservicesbasic.requestToken?pUsername=YOUR_TUM_ID&pTokenName=coursepilot" > ~/tok.xml
```

## Step 2: Activate it

A new token does nothing until you activate it. You have two ways:

- **Email (easiest):** TUMonline sends a mail to your TUM mailbox (not your private one). Open the link in it.
- **TUMonline:** log in and open the token management (Token-Verwaltung). The menu entry is hard to find in the new interface. Use the search in TUMonline and type "Token".

When you activate it, TUMonline asks which rights the token gets. coursepilot needs only **course information (Lehrveranstaltungen)**. Leave the rest off unless you need it.

## Step 3: Store it in `.env`

In the tum-coursepilot folder:

```bash
cp .env.example .env
```

Open `.env` and paste your token:

```
TUMONLINE_TOKEN=your32characters
```

If you used the terminal in step 1, this moves the token from `~/tok.xml` into `.env` without printing it:

```bash
T=$(grep -oP '(?<=<token>)[^<]+' ~/tok.xml) && sed -i "s/^TUMONLINE_TOKEN=.*/TUMONLINE_TOKEN=$T/" .env && rm ~/tok.xml
```

## Step 4: Test it

```bash
python3 scripts/tumonline.py status
```

You should see `Token works.` Done.

## Troubleshooting

| TUMonline says | Meaning | Fix |
|---|---|---|
| `Token ist nicht bestätigt!` | The token exists but you have not activated it. | Do step 2. |
| `Token ist ungültig!` | The token was deleted or never existed. Old tokens also disappear sometimes. | Request a new one (step 1). |
| `Keine Rechte für Funktion ...` | The token lacks the right for this request. | Enable course information in the token management. |
| `Es wurde kein Benutzer zu diesen Benutzerdaten gefunden` | The TUM ID in the URL is wrong. | Check your TUM ID. |
| No activation email | Wrong mailbox, or wrong TUM ID. | Check your TUM mailbox, then the TUM ID. |

## Keep it safe

- Never paste the token into a chat, a screenshot or a commit. `.env` is in `.gitignore` for that reason.
- To revoke it, delete it in the token management. Request a fresh one whenever you like.

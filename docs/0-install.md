# 0. Install the tools

This guide installs the three tools tum-coursepilot needs: Claude Code, Python and Git. It is for anyone starting from zero. Already have them? Skip to the [Quick start](../README.md#quick-start).

You do not need any Python packages. The scripts use only Python's standard library.

## Check what you already have

Open a terminal (macOS: Terminal, Windows: PowerShell, Linux: your terminal) and run:

```bash
claude --version
python3 --version    # Windows: py --version
git --version
```

Every command that prints a version number is done. Install only what is missing.

## Claude Code

You need a paid Claude plan (Pro, Max, Team or Enterprise) or an Anthropic Console account. The free claude.ai plan does not include Claude Code.

| System | Command |
|---|---|
| macOS, Linux, WSL | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Windows (PowerShell) | `irm https://claude.ai/install.ps1 \| iex` |
| macOS with Homebrew | `brew install --cask claude-code` |
| Windows with WinGet | `winget install Anthropic.ClaudeCode` |

Then run `claude` once and log in through the browser. Something went wrong? See the [official setup page](https://code.claude.com/docs/en/setup). It always has the current commands.

## Python 3.8 or newer

| System | Command |
|---|---|
| macOS | `xcode-select --install` (installs Python and Git together), or `brew install python` |
| Windows | `winget install Python.Python.3.13`, or the installer from [python.org](https://www.python.org/downloads/) (tick **"Add python.exe to PATH"**) |
| Ubuntu / Debian | `sudo apt install python3` |
| Fedora | `sudo dnf install python3` |

On Windows the command is usually `py` or `python` instead of `python3`. Use `py scripts/tumonline.py status` wherever the docs say `python3 scripts/tumonline.py status`. Claude figures this out by itself.

## Git

Git downloads the repo and later fetches updates with `git pull`. No Git? Use **Code → Download ZIP** on GitHub instead. It works the same, but you have to download again for updates.

| System | Command |
|---|---|
| macOS | `xcode-select --install`, or `brew install git` |
| Windows | `winget install --id Git.Git -e` (also gives Claude Code a Bash shell) |
| Ubuntu / Debian | `sudo apt install git` |
| Fedora | `sudo dnf install git` |

## Done?

Close and reopen the terminal so it finds the new tools, run the three version checks again, then continue with the [Quick start](../README.md#quick-start).

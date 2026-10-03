# Set up your computer

Do this once per computer, before your first lesson of Module 0. It takes about 20 minutes. This page is the public copy of M74 Academy's setup guide.

| Tool | Why |
|---|---|
| VS Code | Where you read, write code, and type commands |
| uv | Runs Python and every course command; you do **not** install Python yourself |
| Git | Gets the course and its updates, and saves your work |
| GitHub CLI (`gh`) | Signs your computer in to GitHub, so Git can fork and update the course |
| `academy` command | Checks your lessons, opens the course, and checks your setup |

You also need a free [GitHub account](https://github.com/signup).

On a school or work computer where installing is blocked, ask your IT department **before** the first lesson.

## 1. Install VS Code

Download it from [code.visualstudio.com](https://code.visualstudio.com/) and install it. Open it, open the Extensions view (the four-squares icon on the left, or **Ctrl+Shift+X**, **Cmd+Shift+X** on macOS), and install **Python** (by Microsoft).

Now open a terminal inside VS Code: **Terminal → New Terminal**. Type every command below there. On Windows it must say **PowerShell**; choose it from the arrow next to **+** if not.

After each install below you open a **new terminal**, so it finds the new command. On Windows a new terminal is not enough: **quit VS Code completely (File → Exit) and open it again**.

## 2. Install uv

macOS and Linux:

```console
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:

```console
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

These come from the [official uv page](https://docs.astral.sh/uv/getting-started/installation/); if it shows a different command, use that one.

**Close the terminal (trash icon) and open a new one** (on Windows: quit and reopen VS Code), then check:

```console
uv --version
```

It prints a version number. `command not found` (on Windows: `uv : The term 'uv' is not recognized…`) means the terminal is still the old one.

## 3. Install Git

| System | How |
|---|---|
| macOS | Run `git --version` and click **Install** when macOS offers the command line developer tools |
| Windows | Download [Git for Windows](https://git-scm.com/install/) and run the installer with its default choices. If it asks for an administrator password you don't have, ask your IT department |
| Linux | Use your package manager, for example `sudo apt install git` on Ubuntu |

Open a new terminal and check:

```console
git --version
```

Then tell Git who you are. Use your name and an email from your GitHub account (**Settings → Emails**; the `…@users.noreply.github.com` address shown there keeps your email private). Every commit records them:

```console
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Install GitHub CLI and sign in

Git needs your GitHub sign-in to fork the course and push your work. GitHub CLI sets that up.

| System | How |
|---|---|
| macOS | Download the **macOS installer** from [cli.github.com](https://cli.github.com/) and open it. If you already use [Homebrew](https://brew.sh/), `brew install gh` works too |
| Windows | Run `winget install --id GitHub.cli` in the terminal; the first time, winget asks you to accept its terms: type `Y` and press Enter. Or download the **Windows installer** from [cli.github.com](https://cli.github.com/). If it asks for an administrator password you don't have, ask your IT department |
| Linux | Follow the instructions for your distribution on [cli.github.com](https://cli.github.com/) |

Open a new terminal, then sign in:

```console
gh auth login
```

Answer the questions:

1. Where do you use GitHub? **GitHub.com**
2. Preferred protocol? **HTTPS**
3. Authenticate Git with your GitHub credentials? **Yes**
4. How to authenticate? **Login with a web browser**. Note the 8-character code it shows, press **Enter** to open the browser, and type the code there. (Ctrl+C in the terminal cancels the login.)

Check:

```console
gh auth status
```

It says you are logged in to github.com.

## 5. Install the academy command

```console
uv tool install git+https://github.com/m74-academy/academy-cli
```

If uv says its tool folder is not on your `PATH`, run `uv tool update-shell`, then open a new terminal.

The same `academy` command works in every module; `academy update` keeps it and the course current.

## Check

In a **new** terminal, each of these prints a version or a status, not an error:

```console
uv --version
git --version
gh auth status
academy --version
```

`academy --help` lists every command with examples; `academy` alone shows the same.

Your computer is ready. Next: follow **Start here** in the [Module 0 README](https://github.com/m74-academy/module-0#start-here).

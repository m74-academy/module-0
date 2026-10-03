# Fork, clone, and set up a module, step by step

The Module 0 README starts with one command that does all of this:

```console
gh repo fork m74-academy/module-0 --clone
```

This guide explains what it does, and how to do the same by hand.

```text
m74-academy/module-0       the course      → remote: upstream
        │ Fork
        ▼
YOUR-USERNAME/module-0     your fork       → remote: origin
        │ Clone
        ▼
module-0/                  on your computer
```

- **Fork:** your own copy of the course on GitHub. You push your work there. Module 0 is public, so your fork is public too; see the README's use terms.
- **Clone:** that copy downloaded to your computer, in a `module-0` folder.
- **Remotes:** `origin` is your fork; `upstream` is the course. `academy update` gets course updates from `upstream`.

You need [your computer set up](install-uv-and-git.md) first, with `gh auth login` done.

## By hand, in the browser

1. Open the module repository, for example [m74-academy/module-0](https://github.com/m74-academy/module-0), and click **Fork**, then **Create fork**. The result is `YOUR-USERNAME/module-0`.
2. Clone your fork. With GitHub CLI this also adds `upstream`:

   ```console
   gh repo clone YOUR-USERNAME/module-0
   ```

   With Git alone, clone and add `upstream` yourself:

   ```console
   git clone https://github.com/YOUR-USERNAME/module-0.git
   cd module-0
   git remote add upstream https://github.com/m74-academy/module-0.git
   ```

3. Check the remotes from inside the folder:

   ```console
   git remote -v
   ```

   ```text
   origin    https://github.com/YOUR-USERNAME/module-0.git (fetch)
   origin    https://github.com/YOUR-USERNAME/module-0.git (push)
   upstream  https://github.com/m74-academy/module-0.git (fetch)
   upstream  https://github.com/m74-academy/module-0.git (push)
   ```

## Set up the project

In the module folder:

```console
uv sync --locked
```

uv reads three files that come with the module:

| File | Says |
|---|---|
| `.python-version` | which Python |
| `pyproject.toml` | the project and its packages |
| `uv.lock` | the exact tested versions |

It downloads Python if needed and creates `.venv/`. `--locked` stops without changing anything if the lock file doesn't match.

Then check everything:

```console
academy health
```

Every required check prints `OK`, and the last line says `Setup looks good.` A `FAIL` line comes with a fix. `WARN` and `INFO` lines are advice.

## Fix the remotes of an existing clone

`academy health` checks the remotes. If it says **origin is the course, not your fork** (you cloned the course instead of your fork), keep the folder and your work:

```console
gh repo fork --remote
git push -u origin main
```

`gh repo fork --remote` creates your fork (or finds it), renames the course remote to `upstream`, and adds your fork as `origin`. `git push` then saves your work there.

If it says **upstream remote is missing** or **upstream is … not the course**, run the fix it prints, for example:

```console
git remote add upstream https://github.com/m74-academy/module-0.git
```

Run `academy health` again to confirm.

Back to **Start here** in the [Module 0 README](https://github.com/m74-academy/module-0#start-here) for the next step.

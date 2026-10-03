# Get course updates without losing your work

The course changes while you take it. In the module folder, commit your work, then run one command:

```console
git add -A
git commit -m "Save my work"
academy update
```

`academy update` upgrades the `academy` command, and when the course has a newer release it:

1. gets it from the course (`git pull --no-rebase --no-edit upstream main`), keeping your commits and the course's;
2. updates the project's packages (`uv sync --locked`).

Then save the result to your fork:

```console
git push
```

On Windows, a running command can't replace itself: when `academy` has a newer version, it ends with `When this command has finished, run:  uv tool upgrade m74-academy-cli`. Run that once `academy update` is done.

`academy update --check` only reports what is available and changes nothing. The module's `CHANGELOG.md` lists what each release changes.

## When it stops

**Could not reach GitHub to compare:** check your connection, then run `gh auth status`. If Git is not signed in, `gh auth setup-git` fixes it.

`academy update` never commits, discards, or pushes your work for you. It stops in two cases.

**COMMIT FIRST:** you have changes you haven't committed. Commit them, as above, and run `academy update` again.

**COURSE UPDATE STOPPED** with a list of files: you and the course changed the same lines. Nothing is lost.

1. Open each listed file. VS Code shows both versions.
2. Keep your work **and** the course's change, then save.
3. Finish the update:

```console
git add -A
git commit --no-edit
uv sync --locked
git push
```

Never reset or delete your work to make an update apply. Stuck? Open an issue in [m74-academy/module-0](https://github.com/m74-academy/module-0/issues).

## Keep your work

Your fork is yours to keep, under the README's use terms.

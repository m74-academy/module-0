# Lesson 11 — A Script You Can Run

Your functions work when you call them in Python. A coordinator doesn't write Python: they type a command with a folder name and read the answer. This lesson turns a function into a **script**: a file you run from the terminal, which reads what you typed after the command.

## sys.argv and main

`sys.argv` is the list of words on the command line; `sys.argv[0]` is the script itself and the rest are your arguments. Put the work in a `main(argv)` function that takes those words and **returns** a status number, and keep the file runnable but quiet on import with the entry-point **guard**:

```python
import sys


def main(argv):
    if len(argv) != 1:
        print("usage: count-frames FOLDER", file=sys.stderr)
        return 2
    print(f"checking {argv[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
```

`__name__` is `"__main__"` only when you run the file directly, so importing it, as the checks do, runs nothing. `sys.exit` passes the number to the terminal: `0` means everything went fine, anything else means a problem. Other programs read that number. Errors go to `sys.stderr`, the error stream, so they never mix with the real output.

Run a lesson file as a script from the `module-0` folder:

```console
uv run python -m chapter_01.lesson_11 docs/chapters/01-shot-inventory/sample/dump
```

> **Think:** Why does `main` take the words as an argument instead of reading `sys.argv` itself?

<details markdown="1"><summary>Answer</summary>

So a test can call `main(["some/folder"])` with any words it likes and check the result, without starting a new program. The guard is the only line that reads the real command line.

</details>

## Assignment

Open `src/chapter_01/lesson_11.py` and write `main(argv)` for a command that counts image files:

| Situation | Prints | Returns |
|---|---|---|
| Not exactly one argument | `usage: count-frames FOLDER` on stderr | `2` |
| The argument isn't an existing folder | `error: FOLDER is not a folder` on stderr | `2` |
| Otherwise | `N image files` on stdout, counting `.exr` and `.dpx` directly inside | `0` |

Then add the guard, so running the file calls `main` and exits with its result.

```console
academy test 1 11
```

Next: [Lesson 12 — Project: Shot Inventory](12-project.md).

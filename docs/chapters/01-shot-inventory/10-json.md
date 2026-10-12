---
icon: lucide/book-open
tags:
  - JSON
---

# Lesson 1.10 — JSON as Memory

A report printed in the terminal is gone when the window closes. A note in a text file is memory for people, but a program can't read "SH010 comp is missing 1003" reliably. **JSON** is memory that stays after the program ends, for people *and* programs: plain text, readable in any editor, with a structure every programming language can load.

## From Python data to JSON text and back

`json.dumps` turns dictionaries, lists, strings, numbers, `True`/`False`, and `None` into JSON text; `json.loads` turns it back:

```python
import json

shot = {"sequence": "SH010_comp_v002", "frames": [1001, 1002, 1004], "complete": False}
text = json.dumps(shot, indent=2)
print(text)
print(json.loads(text) == shot)
```

```text
{
  "sequence": "SH010_comp_v002",
  "frames": [
    1001,
    1002,
    1004
  ],
  "complete": false
}
True
```

!!! question "Think"

    Two scripts look for missing frames. One takes the number after the word `missing` in the terminal line `SH010_comp_v002: 1001-1004 (missing 1003)`. The other loads the JSON. Then the report wording changes to `(1003 missing)`. Which script breaks, and why?

??? success "Answer"

    The one that reads the terminal text. It found the frame by its place in the sentence, right after the word `missing`, and that place moved. The JSON script still loads the same dictionaries and lists, so the wording of the report never reaches it.

`indent=2` makes it readable. JSON writes `false` and `null` where Python writes `False` and `None`.

Only the types above come back unchanged. A tuple comes back as a list, and a set can't be saved: turn it into a sorted list first.

## Files

`json.dump(data, file)` and `json.load(file)` do the same with an open file. Your assignment uses these two, `dump` and `load`. The `s` stands for *string*: `dumps` and `loads` work with text, `dump` and `load` with a file. Always give the encoding, so the file reads the same on every computer:

```python
import json

shot = {"sequence": "SH010_comp_v002", "frames": [1001, 1002, 1004]}
with open("shots.json", "w", encoding="utf-8") as file:
    json.dump(shot, file, indent=2)

with open("shots.json", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded == shot)
```

```text
True
```

`"w"` opens the file for writing and replaces whatever was in it. To read, open the file without `"w"`. `with` closes the file when the block ends, even if something goes wrong.

This version of `load_json` fails:

```python
import json

def load_json(path):
    return json.load(path)

load_json("shots.json")  # AttributeError: 'str' object has no attribute 'read'
```

!!! question "Think"

    Why does it fail, and what line is missing?

??? success "Answer"

    `json.load` reads from an open file. A path is only text that names the file, and text has nothing to read. Open the file first: `with open(path, encoding="utf-8") as file:`, then `return json.load(file)`.

## Assignment

Open `src/chapter_01/lesson_10.py`.

**1. `save_json(data, path)`** writes `data` to `path` as UTF-8 JSON, indented by 2 spaces.

> Expected: `save_json({"shot": "SH010"}, path)` writes:
>
> ```json
> {
>   "shot": "SH010"
> }
> ```

**2. `load_json(path)`** returns the data from a JSON file.

> Expected: `load_json(path)` → `{"shot": "SH010"}`

Check your work:

```console
academy test 1 10
```

## Further reading

- [Saving structured data with `json`](https://docs.python.org/3/tutorial/inputoutput.html#saving-structured-data-with-json) (Python tutorial): the same `dump` and `load` steps, with the `with` statement explained earlier on the same page.
- [Python to JSON conversion table](https://docs.python.org/3/library/json.html#py-to-json-table) (Python reference): which Python type becomes which JSON type.
- [Introducing JSON](https://www.json.org/json-en.html) (json.org): the whole format on one page, with a diagram for each kind of value.
- [`json`: JavaScript Object Notation](https://pymotw.com/3/json/index.html) (Python Module of the Week): more examples, including tuples coming back as lists.

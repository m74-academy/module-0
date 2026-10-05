---
icon: lucide/book-a
---

# Glossary

Every term here is also explained in the lesson that first uses it; the link takes you there.

### Exit code

The number a program returns when it finishes: `0` for success, anything else for a problem. Other programs read it. [A Script You Can Run](chapters/01-shot-inventory/11-script.md)

### f-string

A string with `f` before the quote, where `{value}` is replaced by the value and `{frame:04d}` pads a number. [Building Names with f-strings](chapters/01-shot-inventory/02-f-strings.md)

### Frame

One still image of a shot. Frames are numbered in order, such as `1001`. [Names Carry Data](chapters/01-shot-inventory/01-names-carry-data.md)

### Frame padding

Writing a frame number with a fixed number of digits, filled with leading zeros: frame `7` as `0007`. [Building Names with f-strings](chapters/01-shot-inventory/02-f-strings.md)

### JSON

A text format for structured data that people and programs can both read. Python reads and writes it with the `json` module. [JSON as Memory](chapters/01-shot-inventory/10-json.md)

### Sequence

All the frames of one shot, task, and version, such as `SH010_comp_v002`: everything in a frame's name before the frame number. [Names Carry Data](chapters/01-shot-inventory/01-names-carry-data.md)

### Set

A Python collection that holds each value once and can be compared with another: `expected - found` gives what's missing. [Sets: Finding Missing Frames](chapters/01-shot-inventory/06-sets.md)

### Shot

One continuous piece of a film, named such as `SH010`. [Names Carry Data](chapters/01-shot-inventory/01-names-carry-data.md)

### Task

The kind of work a file contains, such as `comp` (compositing) or `roto`. [Names Carry Data](chapters/01-shot-inventory/01-names-carry-data.md)

### Version

A numbered delivery of the same work, such as `v002`. Each new delivery gets the next version. [Names Carry Data](chapters/01-shot-inventory/01-names-carry-data.md)

## Pages by term

Each lesson lists the terms it defines as tags at the bottom of the page. Every tag, with its pages:

<!-- material/tags -->

---
icon: lucide/map
---

# Chapter 1 — Shot Inventory

A visual-effects studio produces thousands of image files a day, and their names are the first thing anyone reads. This chapter starts with a folder where files from several shots have been dumped together, and ends with a script that sorts out what is there, what is missing, and what doesn't belong. Each lesson teaches one piece of Python through that problem, with a function in `src/chapter_01/` that you check with `academy test 1 LESSON`.

1. [Names Carry Data](01-names-carry-data.md) — read a messy folder by hand, and see what a filename tells you.
2. [Building Names with f-strings](02-f-strings.md) — build a frame filename from its parts, with padding.
3. [Splitting a Name into Parts](03-splitting.md) — take a filename apart again with string methods.
4. [Numbers from Text](04-numbers.md) — turn `"1001"` and `"v002"` into numbers you can calculate with.
5. [Frame Ranges and List Comprehensions](05-ranges.md) — list every frame a sequence should have.
6. [Sets: Finding Missing Frames](06-sets.md) — compare what should be there with what is.
7. [Sorting Frames as Numbers](07-sorting.md) — put frames in order, and write a range as `1001-1004`.
8. [Dictionaries: Grouping by Sequence](08-grouping.md) — sort a mixed listing into sequences.
9. [Listing a Folder with `os`](09-folders.md) — read real filenames from a folder.
10. [JSON as Memory](10-json.md) — save results in a file that people and programs can read.
11. [A Script You Can Run](11-script.md) — turn functions into a command.
12. [Capstone: Shot Inventory](../../capstone.md) — put it all together.

The sample folder, `docs/chapters/01-shot-inventory/sample/` in your project, holds the messy delivery the lessons and the project use. Its `.exr` files are tiny text files with image names, not real images.

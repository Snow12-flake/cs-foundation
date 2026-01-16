
## `week3/project6_search_engine/README.md`

```md
# File Search Engine

## Description
Command-line search engine that indexes all .txt files in a folder using os.walk() and searches with an inverted index dictionary.  
Week 3 Project 6 from CS Foundations course.

## Features
- Recursive directory traversal with os.walk()
- Inverted index: {word: set(filenames)}
- Case-insensitive search
- Multiple search queries via REPL

## Technologies Used
- Python
- os module

## How to Run
```bash
cd week3/project6_search_engine
python search_engine.py
# Enter folder path: test_files
# Search: "python" → finds doc1.txt, doc2.txt

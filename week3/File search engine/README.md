
**`week3/File Search Engine/README.md`**
```md
# File Search Engine

## Description
Command-line search engine that indexes all .txt files in a folder using os.walk() 
and builds an inverted index mapping words to filenames.

## Features
- Recursive directory traversal (os.walk)
- Case-insensitive word tokenization
- Inverted index: {word: set(filenames)}
- Interactive REPL search interface

## Technologies Used
- Python os module, defaultdict

## How to Run
```bash
cd week3/"File Search Engine"
python search_engine.py
# Enter: test_files/
# Search: Python → {'doc1.txt'}



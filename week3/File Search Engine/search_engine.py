import os

def build_index(folder_path):
    """
    WALK folder with os.walk, READ .txt files, BUILD inverted index:
    {word: set(filenames containing word)} - CASE INSENSITIVE
    """
    index = {}  # Dictionary: word -> set of files
    print(f" Indexing folder: {folder_path}")
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):  # Only process text files
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read().lower()  # LOWERCASE for case-insensitive
                        words = content.split()     # SPLIT on whitespace
                    
                    for word in words:
                        word = word.strip('.,!?;:-()[]{}"\'')  # CLEAN punctuation
                        if len(word) > 2:  # Ignore short words
                            if word not in index:
                                index[word] = set()
                            index[word].add(file)  # ADD filename to set
                            
                except Exception as e:
                    print(f" Skip {file}: {e}")
    
    print(f" Indexed {len(index)} unique words from {len(os.listdir(folder_path))} files")
    return index

def search_files(index, query):
    """
    SEARCH index for query word, RETURN matching files
    """
    query = query.lower().strip('.,!?;:-()[]{}"\'')
    matches = index.get(query, set())
    return matches

if __name__ == "__main__":
    # STEP 1: Get folder path from user
    folder_path = input(" Enter folder path containing .txt files: ").strip()
    
    if not os.path.exists(folder_path):
        print(" Folder not found!")
        exit()
    
    # STEP 2: Build index (dict: word -> set(files))
    index = build_index(folder_path)
    
    # STEP 3+: REPL loop for multiple searches
    while True:
        query = input("\n🔍 Search term (or 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            break
        
        matches = search_files(index, query)
        if matches:
            print(f" Found in {len(matches)} files:")
            for file in sorted(matches):
                print(f"   - {file}")
        else:
            print(" No matches found")

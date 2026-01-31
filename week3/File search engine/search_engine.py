import os
from collections import defaultdict

def create_index(folder_path):
    index = defaultdict(set)
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        words = f.read().lower().split()
                        for word in words:
                            index[word].add(file)
                except:
                    pass
    return index

def search_files(index, query):
    return index.get(query.lower(), set())

if __name__ == "__main__":
    folder = input("Folder path: ")
    index = create_index(folder)
    while True:
        query = input("Search (quit to exit): ")
        if query == 'quit': break
        results = search_files(index, query)
        print(f"'{query}' found in: {results}")

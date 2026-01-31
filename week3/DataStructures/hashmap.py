class HashMap:
    def __init__(self):
        self.buckets = [[] for _ in range(10)]
    
    def _hash(self, key):
        return hash(key) % 10
    
    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

if __name__ == "__main__":
    hm = HashMap()
    hm.set("age", 25)
    print(hm.get("age"))  # 25


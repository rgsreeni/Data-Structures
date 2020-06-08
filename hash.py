class hash:
    def __init__(self):
        self.slot = [[None] for _ in range(10)]

    def _hash(self, key):
        return int(key % 10)

    def put(self, key, value):
        hashval = self._hash(key)
        if self.slot[hashval] == [None]:
            self.slot[hashval] = [(key, value)]
        else:
            length = len(self.slot[hashval])
            i = 0
            exist = False
            while i < length:
                if self.slot[hashval][i][0] == key:
                    del self.slot[hashval][i]
                    self.slot[hashval].append((key, value))
                    exist = True
                i += 1
            if not exist:
                self.slot[hashval].append((key, value))

    def get(self, key):
        hashval = self._hash(key)

        length = len(self.slot[hashval])
        i = 0
        exists = False
        while i < length:
            if self.slot[hashval][i][0] == key:
                return self.slot[hashval][i][1]
                exists = True
            i += 1

        if not exists:
            print("Error : Not Assigned")

    def printh(self):
        for i in range(len(self.slot)):
            print("\n", i, end=" ")
            for j in range(len(self.slot[i])):
                print("->", end=" ")
                print(self.slot[i][j], end="")

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = hash()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
h.printh()
print("\n")
print(h.slot)

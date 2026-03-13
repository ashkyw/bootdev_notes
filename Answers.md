CH 12 L5:
```py
class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = key, value

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {i}: {str(v)}\n"
            else:
                final += f" - {i}: None\n"
        return final
```

CH 12 L6:

```py
class HashMap:
    def get(self, key):
        try:
            i = self.key_to_index(key)
            return self.hashmap[i][1]
        except:
            raise Exception("sorry, key not found")


    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final

```

CH 12 L7:
1

CH 12 L8:
2

CH 12 L9:

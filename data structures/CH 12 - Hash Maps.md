# Hashmaps

A [hash map](https://en.wikipedia.org/wiki/Hash_table) or "hash table" is a data structure that maps keys to values:

    "bob" -> "ross"
    "pablo" -> "picasso"
    "leonardo" -> "davinci"

The lookup, insertion, and deletion operations of a hashmap have an average computational cost of `O(1)`. Assuming you know the key, nothing beats a hashmap! A Python dictionary is an example of a hashmap. See, you already know what a hashmap is!

### Under the Hood

While hashmaps are simple to use - you're already proficient with them if you know how to use a Python dictionary - the _implementation_ is a bit trickier.

Hashmaps are built on top of arrays (or in the case of ours, a Python list). They use a [hash function](https://www.boot.dev/blog/cryptography/how-sha-2-works-step-by-step-sha-256) to convert a "hashable" key into an index in the array. From a high-level, all that matters to us is that the hash function:

    1. Takes a key and returns an integer.
    2. Always returns the same integer for the same key.
    3. Always returns a valid index in the array (e.g. not negative, and not greater than the array size)

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/hash%20map.png)

Ideally the hash function hashes each key to a unique index, but most hash table designs employ an _imperfect_ hash function, which might cause hash [collisions](https://en.wikipedia.org/wiki/Hash_collision) where the hash function generates the same index for more than one key. An example of a collision in the above example would be "bob" and "leonardo" both hashing to index 3. Ideally "leonardo" would hash to some other index, like 2.

Such collisions are typically accommodated for, and are _not_ a problem in practice.

### Hash Function

Let's build a toy hash map in Python. In the real world, you would almost always use the built-in Python dictionary if you need a hash map. However, just using a dictionary doesn't teach us about what's going on under the hood!

```py
class HashMap:
    def key_to_index(self, key):
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)
```

### Insert

Now that we have some building blocks for our hashmap, we need a way to start inserting values.

```py
class HashMap:
    def insert(self, key, value):
        self.hashmap[self.key_to_index(key)] = key, value
    
    def insert(self, key, value):
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

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

### Get

Now that we can insert our users and their records into our hashmap, we need a way to retrieve that information when requested!

```py
class HashMap:
    def get(self, key):
        try:
            i = self.key_to_index(key)
            return self.hashmap[i][1]
        except:
            raise Exception("sorry, key not found")

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

### Hash Map Review:

Hashmaps are awesome. They are simple to use and have an average computational cost of `O(1)` for lookup, insertion, and deletion operations.

In Python, that means dictionaries. In Go, it means maps. In JavaScript, it means object literals. The point is, if you need an in-memory key-value store, hashmaps are awesome, and every language tends to have a built-in implementation.

### Properties of a _Good_ Hash Map

* **Fast Lookups**: Hashmaps have an average time complexity of `O(1)` for lookups, insertions, and deletions.
* **Unordered**: Hashmaps (typically) do not guarantee any particular order of keys.
* **No Ranging**: While hashmaps are great for lookups, they don't provide the ability to look into a _range_ of keys (e.g. the largest ten keys). That's one reason production databases like Postgres use binary trees for indexing.
* **Collision Resistant**: Hashmaps are built on top of arrays and use a hash function to convert a key into an index. Production-ready implementations (like Python dictionaries) handle hash collisions and make them a non-issue in practice.
* **Hashable Keys**: Keys must be hashable. This means they must be immutable and have a consistent hash value. For example, in Python, a tuple can be a key, but a list cannot.
* **Efficient Resizing**: When a hashmap's capacity is exceeded, it dynamically resizes (usually by doubling in size) and rehashes the elements. A good hashmap manages this resizing efficiently, minimizing performance hits.
* **Uniform Distribution**: A good hash function ensures keys are distributed evenly across the hashmap's underlying array, minimizing the number of collisions and optimizing lookup speed.

### Resizing

In the current implementation of `HashMap`, our hashmap has a lot of collisions. This is because we are using a fixed size for our hashmap.

To reduce the chances of a collision, we can increase the number of slots in our hashmap. This is called resizing. This will not eliminate all possible collisions, but it will help reduce the chance of one happening.

When resizing, we create a new hashmap with a larger number of slots. Then, we re-insert all the key-value pairs from the old hashmap into the new hashmap.

```py
class HashMap:
    def insert(self, key, value):
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        if self.current_load() < 0.05:
            return
        else:
            temp_map = self.hashmap
            new_hashmap = [None for index in range(len(self.hashmap)*10)]
            self.hashmap = new_hashmap
            for item in temp_map:
                if item is not None:
                    key, value = item
                    self.hashmap[self.key_to_index(key)] = item
            
    def current_load(self):
        if len(self.hashmap) == 0:
            return 1

        counter = 0
        for i in range(len(self.hashmap)):
            if self.hashmap[i] is not None:
                counter += 1

        return counter / len(self.hashmap)

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
                final += f" - {str(v)}\n"
        return final

```

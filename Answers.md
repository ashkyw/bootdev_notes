Data Structures: 

CH8 L1 Answer:
#2

CH8 L2 Answer:

```py
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

```

CH8 L3 Answer:

#4

CH8 L4 Answer:

#1 (maybe)

CH8 L5 Answer:

#3

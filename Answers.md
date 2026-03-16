CH13 L 5:
```py
class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level.keys():
            words.append(current_prefix)
        sorted_list = list(sorted(current_level.keys()))
        for letter in sorted_list:
            if letter != self.end_symbol:
                next_prefix = current_prefix + letter
                self.search_level(current_level[letter], next_prefix, words)
        
        return words
    
    def words_with_prefix(self, prefix):
        matching_words = []
        current_level = self.root
        for char in prefix:
            if char not in current_level:
                return []
            current_level = current_level[char]
        self.search_level(current_level, prefix, matching_words)
        
        return matching_words

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
```

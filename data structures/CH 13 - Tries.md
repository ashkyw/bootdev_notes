# Trie

[Trie](https://en.wikipedia.org/wiki/Trie) are one of my favorite data structures, I've used them often in the past for [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing) tasks. In Python, a trie is easily implemented as a nested tree of dictionaries where each key is a character that maps to the next character in a word. For example, the words:

  * hello
  * help
  * hi

Would be represented as:
```py
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
```
The `*` character (paired with `True` instead of a dictionary) is used to indicate the end of a word.

A trie is also often referred to as a "prefix tree" because it can be used to efficiently find all of the words that start with a given prefix.

Add function in a Trie:

```py
class Trie:
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
```

Exists function in a Trie:

```py
class Trie:
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
```

### Prefix Matching

Tries tend to be most useful for prefix matching. For example, if you wanted to find all the words in a dictionary that start with a given prefix, a trie works great! Autocomplete, keyword search, and spellcheck are all good examples of where a trie can be useful.

Remember, a hash table is only good for exact matches, whereas a trie allows you to look up all of the words that match a given prefix. For example, given this trie:
```py
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
                        "*": True
                    }
				},
				"p": {
                    "*": True
                }
			}
		},
        "a": {
			"r": {
				"d": {
					"*": True
				}
			}
		}
	}
}
```
We could quickly find all the words that start with "hel" and get:

* hello
* help

Adding get prefix for text prediction functionality:

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

### Find Matches

Tries are super efficient when it comes to finding substrings in a large document of text. For LockedIn, we want to be able to find all of the instances of bad words in chat messages and filter them out.

If we just split on whitespace and matched against a dictionary, we would miss substrings. For example, if we had the word "darn" in our dictionary, we would allow the word "darnit" to slip through undetected. That's why we'll use a trie.

Adding match functionality:

```py
class Trie:
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
```

Adding longest common prefix functionality:

```py
class Trie:
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key == self.end_symbol:
                    break
                children.append(key)
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
```

Adding advanced matching to identify swapped letters i.e. a : @:

```py
class Trie:
    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
```

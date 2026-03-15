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

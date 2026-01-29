# Closure

A [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)) is a function that references variables from outside its own function body.  The function definition and *its environment* are bundled together into a single entity.

Put simply, a closure is just a function that **keeps track of some values** from the place where it was *defined*, no matter where it is executed later on.

Example

The `concatter()` function returns a function called `doc_builder` (yay higher-order functions!) that has a reference to an *enclosed* `doc` value.
```py
def concatter():
	doc = ""
	def doc_builder(word):
		# "nonlocal" tells Python to use the 'doc'
		# variable from the enclosing scope
		nonlocal doc
		doc += word + " "
		return doc
	return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive
```
When `concatter()` is called, it creates a new "stateful" function that *remembers* the value of its internal `doc` variable. Each successive call to `harry_potter_aggregator` appends to that same `doc`.

#nonlocal

Python has a keyword called [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) that's required to modify a variable from an enclosing scope. Most programming languages don't require this keyword, but Python does.

Another example of closure and nonlocal:

```py
def word_count_aggregator():
    count = 0
    def word_count(doc):
        for item in doc.split():
            nonlocal count
            count += 1
        return count
    return word_count
```

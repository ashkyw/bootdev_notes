# Regex

[Regex](https://docs.python.org/3/library/re.html), or "regular expressions" are a programming-language-agnostic way of searching for patterns in text.

They're famous for being hard to read, but occasionally, they are the simplest way to solve a problem.

![](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/regex.png)

In Python we can use the [`re` module](https://docs.python.org/3/library/re.html) to work with regex. It has a [findall](https://docs.python.org/3/library/re.html#re.findall) function that will return a lsit of all the matches in a string. 

### Regex for a Single Word
```py
import re

text = "I'm a little teapot, short and stout. Here is my handle, here is my spout."
matches = re.findall(r"teapot", text)
print(matches) # ['teapot']
```

* `r"teapot"` is a regex pattern
* The `r` tells Python to treat the string as a "raw" string, which means we don't have to use escape sequences for backslashes. [Escaping](https://en.wikipedia.org/wiki/Escape_sequence) in Python involves using a backslash `(\)` to nesure special characters are treated as literal characters
* The pattern `teapot` will match any exact occurences of the word "teapot" in the input.

### Regex for Phone Number
```py
text = "My phone number is 555-555-5555 and my friend's number is 555-555-5556"
matches = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print(matches) # ['555-555-5555', '555-555-5556']
```

* `\d` matches any digit
* `{3}` means "exactly three of the preceding character"
* `-`  is just a literal `-` that we want to match

### Regex for Text Between Parentheses
```py
text = "I have a (cat) and a (dog)"
matches = re.findall(r"\((.*?)\)", text)
print(matches) # ['cat', 'dog']
```

* `\(` and `/)`are escaped parentheses that we want to match
* `(` and `)` is a [capture group](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Capturing_group) meaning it groups the matched text, allowing us to reference or extract it separately.
* `.*?` matches any number of characters (except for [line terminators](https://en.wikipedia.org/wiki/Newline)) between the parentheses

### Regex for Emails Multiple Capture Groups
```py
text = "My email is lane@example.com and my friend's email is hunter@example.com"
matches = re.findall(r"(\w+)@(\w+\.\w+)", text)
print(matches)  # [('lane', 'example.com'), ('hunter', 'example.com')]
```

* `\w` macthes any word character ([alphanumeric](https://en.wikipedia.org/wiki/Alphanumericals) characters and underscores)
* `+` means "one or more peceding character"
* `@` is just a literal `@` symbol that we want to match
* `\.` is a literal `.` that we want to match (The `.` is a special character in regex, so we escape it with a leading backslash)

### Negative Lookbehind
Sometimes you need to match something that is NOT preceded by something else. This is where a negative lookbehind comes in handy.

```py
text = "The word cat appears here, but not in concat"
matches = re.findall(r"(?<!con)cat", text)
print(matches)  # ['cat']
```

* `(?<!con)cat` is a negative lookbehind that matches "cat" only if it's NOT preceded by "con"
* This allows us to match "cat" in "concat"
* The general syntax is `(?<!pattern)` where `pattern` is what you don't want to see before your match

# Testing Regex

[regexr.com](https://regexr.com/) is useful for interactive Regex testing. It breaks down each part of the pattern and explains what it does.

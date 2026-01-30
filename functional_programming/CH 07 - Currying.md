# Currying

Function [currying](https://en.wikipedia.org/wiki/Currying) is a specific *kind* of function transformation where we translate a single function that accepts multiple arguments into multiple *functions* that each accept a *single* argument.

This is a "normal" 3-argument function:

```py
box_volum(3,4,5)
```

This is a "curried" *series of functions* that does the same thing:

```py
box_volume(3)(4)(5)
```

Another example that includes the implementations:

```py
def sum(a, b):
  return a + b

print(sum(1, 2))
# prints 3
```

And curried:

```py
def sum(a):
  def inner_sum(b):
    return a + b
  return inner_sum

print(sum(1)(2))
# prints 3
```

The `sum` function only takes a *single* input, `a`. It returns a *new* function that takes a single input, `b`. This new function when called with a value for `b` will return the sum of `a` and `b`. 

Another example of currying:
```py
def converted_font_size(font_size):
    def converted_doc(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return converted_doc
```

So why would we *ever* want to do the more complicated thing? Well, currying can be used to **change a function's signature** to make it conform to a specific shape. For example:
```py
def colorize(converter, doc):
  # ...
  converter(doc)
  # ...
```
The `colorize` function accepts a function called `converter` as input, and at some point during its execution, it calls `converter` with a single argument. That means that it expects converter to accept exactly one argument. So, if I have a conversion function like this:

```py
def markdown_to_html(doc, asterisk_style):
  # ...
```
I can't pass `markdown_to_html` to `colorize` because `markdown_to_html` wants *two* arguments. To solve this problem, I can curry `markdown_to_html` into a function that takes a single argument:

```py
def markdown_to_html(asterisk_style):
  def asterisk_md_to_html(doc):
    # do stuff with doc and asterisk_style...

  return asterisk_md_to_html

markdown_to_html_italic = markdown_to_html('italic')
colorize(markdown_to_html_italic, doc)
```

Another example of currying:
```py
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            doc_split = doc.split()
            count = 0
            for item in doc_split:
                if sequence in item:
                    count +=1
            return count
        
        return with_length
    return with_char

```

Another example of currying:
```py
def create_markdown_image(alt_text):
    enclosed_alt_text = f"![{alt_text}]"

    def add_url(url):
        escaped_url = url.replace("(", "%28").replace(")", "%29")
        image_syntax = enclosed_alt_text + f"({escaped_url})"

        def add_title(title=None):
            if title:
                return image_syntax[:-1] + f' "{title}")'
            return image_syntax

        return add_title

    return add_url
```

Another example of currying:
```py
def new_resizer(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize_image(width, height):
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height

        return resize_image

    return set_min_size
```

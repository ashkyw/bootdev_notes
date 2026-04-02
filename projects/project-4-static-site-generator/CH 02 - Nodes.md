# TextNode

We're going to need a way to represent all the different types of [inline](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) text. We're going to be parsing Markdown text, and outputting it to HTML, so we need an intermediate representation of the text in our code.

When I say "inline" I just mean text that is part of a larger block of text. For us, this includes:
* text (plain)
*  `**Bold text**`
*  `_ Italic text_`
*  `Code text`
*  links, in this format: `[anchor text](url)`
*  images, in this format: `![alt text](url)`

Everything else we're considering [block level](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements), like headings, paragraphs, and bullet lists, and we'll handle those later.

### TextNode Tests

[Unit tests](https://en.wikipedia.org/wiki/Unit_testing) are a way to verify that the code you write works as expected. In other Boot.dev courses, you write code that passes the unit tests provided. As a developer, you'll be expected to write your _own_ tests to ensure that your code, "units", work as expected.

It can feel like a lot of extra work...
... but it's often worth it, especially if the logic you're testing is particularly complex while simultaneously easy to test (e.g. it doesn't rely on external stuff like files or the network). Once you have some good tests, you can run them whenever you make changes to ensure you don't break anything.

[unittest library documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual)

# LeafNode

Time to render some HTML strings!

A `LeafNode` is a type of `HTMLNode` that represents a single HTML tag with _no children_. For example, a simple `<p>` tag with some text inside of it:
```html
<p>This is a paragraph of text.</p>
```
We call it a "leaf" node because it's a "leaf" in the tree of HTML nodes. It's a node with no children. In this next example, `<p>` is not a leaf node, but `<b>` is.
```html
<p>
  This is a paragraph. It can have a lot of text inside tbh.
  <b>This is bold text.</b>
  This is the last sentence.
</p>
```

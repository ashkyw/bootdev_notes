# TextNode

We're going to need a way to represent all the different types of [inline](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) text. We're going to be parsing Markdown text, and outputting it to HTML, so we need an intermediate representation of the text in our code.

When I say "inline" I just mean text that is part of a larger block of text. For us, this includes:
* text (plain)
*  `**Bold text**`
*  `_ Italic text_`
*  `` Code text``
*  links, in this format: `[anchor text](url)`
*  images, in this format: `![alt text](url)`

Everything else we're considering [block level](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements), like headings, paragraphs, and bullet lists, and we'll handle those later.

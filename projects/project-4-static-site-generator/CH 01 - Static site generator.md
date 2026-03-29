# HTML

The primary output of a static site generator is [HTML(HyperText Markup Language)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics), because HTML containstt all the _content_ of a web page.

HTML is a simple language for _structuring content_. It's _not a "programming" language_ in that sense that it doesn't have variables, loops, or conditionals.

HTML is a way to format text, images, links, and other media so that a web browser can render it in a [GUI](https://en.wikipedia.org/wiki/Graphical_user_interface). Here's a simple HTML file:

```html
<html>
  <head>
    <title>Why Frontend Development Sucks</title>
  </head>
  <body>
    <h1>Front-end Development is the Worst</h1>
    <p>
      Look, front-end development is for script kiddies and soydevs who can't
      handle the real programming. I mean, it's just a bunch of divs and spans,
      right? And css??? It's like, "Oh, I want this to be red, but not thaaaaat
      red." What a joke.
    </p>
    <p>
      Real programmers code, not silly markup languages. They code on Arch
      Linux, not macOS, and certainly not Windows. They use Vim, not VS Code.
      They use C, not HTML. Come to the
      <a href="https://www.boot.dev">backend</a>, where the real programming
      happens.
    </p>
  </body>
</html>
```

HTML is a tree-like structure where each "tag" (e.g. `<p>`, the bits enclosed in angle brackets) can contain other tags, and the whole thing is enclosed in an outermost `<html>` tag. Let's break down the structure of this HTML file:

* `<html>` is the root element of the document
* `<head>` contains [metadata](https://en.wikipedia.org/wiki/Metadata) about the document. Anything in the `<head>` is _not rendered visibly_ in the browser window.
  * `<title>` is the title of the document, which is displayed in the browser tab.
* `<body>` contains the content of the document, which is what _is_ rendered in the browser window.
  * `<h1>` is a top-level heading
  * `<p>` is a paragraph of text
  * `<a>` is a hyperlink. The `<href>` [attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes) is the URL the link points to.m Attributes are key-value pairs that provide additional information about an element, like `href="https://www.boot.dev"`.

# CSS

[CSS (Cascading Style Sheets)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) is another "not-really-a-programming-language" that styles [HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). It's a way to dress up your HTML with colors, fonts, responsive layouts, animations, etc.
```css
/* Make all <h1> HTML elements red */
h1 {
  color: red;
}
```
Or maybe we want the max-width of our paragraphs to be 50% of the screen width:
```css
/* Make all <p> HTML elements 50% of the screen width */
p {
  max-width: 50%;
}
```

# Markdown

**Writing HTML by hand sucks**. Even if you're a grubby front-end programmer, you probably don't want to write entire documents in raw HTML.

**Writing [Markdown](https://www.markdownguide.org/getting-started/) is pure bliss**. Markdown is a less-verbose markup language designed for _ease of writing_. The trouble is web browsers don't understand Markdown. They only understand HTML and CSS. **The #1 job of a static site generator is to convert Markdown into HTML**.

Instead of writing a verbose HTML list:

```html
<ul>
  <li>I really</li>
  <li>hate writing</li>
  <li>in raw html</li>
</ul>
```

We can write this in Markdown

```md
- I really
- hate writing
- in raw html
```

Our static site generator will take a directory of Markdown files (one for each web page), and build a directory of HTML files. Because we're not savages, we'll also include a single CSS file to style the site.

> [!NOTE]
>All lessons on Boot.dev are written in Markdown!
>

### Architecture

![Static site architecture](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Static%20site%20generator%20architecture.png)

The flow of data through the full system is:

  1. Markdown files are in the `/content` directory. A `template.html` file is in the root of the project.
  2. The static site generator (the Python code in `src/`) reads the Markdown files and the template file.
  3. The generator converts the Markdown files to a final HTML file for each page and writes them to the `/public` directory.
  4. We start the built-in Python HTTP server (a seperate program, unrelated to the generator) to serve the contents of the `/public` directory on `http://localhost:8888` (our local machine).
  5. We open a browser and navigate to `http://localhost:8888` to view the rendered site.

### How the SSG works

The vast majority of our coding will happen in the `src/`directory because almost all of the work is done in steps 2 and 3 above. Here's a rough of what the final program will do when it runs:

  1. Delete everything in the `/public` directory.
  2. Copy any static assets (HTML template, images, CSS, etc.) to the `/public` directory.
  3. Generate an HTML file for each Markdown file in the `/content` directory. For each Markdown file:
     1. Open the file and read its contents.
     2. Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
     3. Convert each block into a tree of `HTMLNode` objects. For inline elements (like bold text, links, etc.) we will convert:
        * Raw markdown -> `TextNode` -> `HTMLNode`
     4. Join all the `HTMLNode` blocks undre on large parent `HTMLNode` for the pages.
     5. Use a recursive `to_html()` method to convert the `HTMLNode` and all its nested nodes to a giant HTML string and inject it in the HTML template.
     6. Write the full HTML string to a file for that page in the `/public` directory.

### How we're gonna build it:

We're not going to _build_ the program in the same order that it _runs_... that's often not the best way to build large projects. Instead, we'll tackle individual problems that we know we'll need to solve and use unit tests to make sure they work as expected. Then we'll put the pieces together into a working program as we get closer to the end. 

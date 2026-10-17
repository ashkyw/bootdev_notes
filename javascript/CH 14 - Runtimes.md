# JavaScript Runtimes

[JavaScript Runtimes Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/js-runtimes-1920x1080.mp4)

A runtime environment is _where your program runs_. The runtime you choose will determine things like:
  * What APIs are available to your code (fetch, canvas, etc.)
  * How your code is executed (JIT compiled vs interpreted)
  * What dependencies you'll need in production
  * Whether you run on the backend (a serve) or the frontend (a browser or mobile app)

## Examples of Runtimes
  * The browser (we try to pretend they're the same, but in reality different browsers are different runtimes)
  * [Node.js](https://nodejs.org/en/)
  * [A web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) (within a browser)
  * [Deno.js](https://deno.land/)
  * [Bun](https://bun.sh/)

Originally, JavaScript _only_ ran in browsers. Today, it runs almost everywhere.

## Which Runtime Should I use?
If you're doing frontend development, congratulations! You're using the browser. You likely have to support all the major browsers, so you'll need to know what APIs are available for each.

If you're doing backend development, you get to choose. Node.js is the oldest & most popular. Deno & Bun are newer & less mature, but have some cool features (like native Typescript support) & claim to be faster. In reality, they're all very similar to work with. You don't need to "learn" a runtime to be able to work with it. If you understand JavaScript, you can work with any of them.

# Node.js
If you've used Python before, you're familiar with running a Python script like this:
```py
python main.py
```
Similarly, if you install [Node.js](https://nodejs.org/en/download/) toolchain on your local machine, you'll be able to run
```js
node main.js
```
Before Node, the only way to run JavaScript code was in the browser. Of course, you can still do that using [your browser's dev tools!](https://developer.chrome.com/docs/devtools/console/javascript/)

## NVM

Node Version Manager (NVM) makes it easy to:
 * Install multiple versions of Node
 * Update your Node version
 * Keep your Node version configurations separate on a per-project basis

It's kinda like `pyenv` for Python.

# NPM
Now that `node` is working, it's important to understand that... you probably won't use it directly very often. Instead, you'll use `npm` (Node Package Manager) to install & manage packages.

[`npm`](https://www.npmjs.com/) is a package manager for JavaScript. It's the world's largest software registry, with over 1.3 million packages of code. It's the home of many useful libraries such as:
 * [is-even](https://www.npmjs.com/package/is-even)
 * [cowsay](https://github.com/piuccio/cowsay)
 * [left-pad](https://www.npmjs.com/package/left-pad)

If you're familiar with Python, `npm` is similar to `pip` or `uv`. If you're familiar with Go, `npm` is similar to `go get`.
# DOM
It's impossible to talk about JavaScript without mentioning its original use case: doing fancy stuff in the browser.

The DOM (Document Object Model) is just an in-memory representation of an HTML document, you know, the thing that front-end devs suffer through working with on a daily basis. The [static site generator project](https://www.boot.dev/courses/build-static-site-generator-python) you did kinda built DOM from scratch when you converted markdown into in-memory nodes.

## Okay, so what's it look like?
Let's pretend we have this super cool HTML file that represents a homepage:
```html
<html>
  <head>
    <title>Princess Mononoke Fan Club</title>
  </head>

  <body>
    <h1 id="mainHeading">A Fan Club for Mononoke Enjoyers</h1>
    <p>
      Join us in riveting discussion about the philosophical truths and untruths
      revealed in the greatest metaphor of modern times.
    </p>
    <p>Every Tuesday at 7pm EST.</p>
    <button id="joinButton">Join the Fun</button>
  </body>
</html>
```
When this HTML file is loaded into a browser, the browser creates a DOM in memory that our JavaScript code can interact with through a global object called [`document`](https://developer.mozilla.org/en-US/docs/Web/API/Document). For example, let's say I wanted to change the text of the `<h1>` (header) & the style of the `<p>` (paragraph) elements when a user clicks the "Join the Fun" button.

First, we need to define a function that will be called when a button is clicked:
```js
function onJoinClick() {
  // ...
}
```
Inside the function, we can access the `h1` element by the `id` attribute we gave it & change its text content:
```js
function onJoinClick() {
  document.getElementById("mainHeading").textContent = "Welcome to the Club!";
}
```
Next, let's say we want to change the color of the text in the paragraph. We can access all the `p` elements & change their `style` properties:
```js
function onJoinClick() {
  document.getElementById("mainHeading").textContent = "Welcome to the Club!";
  const paragraphs = document.getElementsByTagName("p");
  for (const p of paragraphs) {
    p.style.color = "red";
  }
}
```
Finally, we need to register the function to be called when the button is clicked by adding an event listener:
```js
document.getElementById("joinButton").addEventListener("click", onJoinClick);
```
Now, when the user clicks the "Join the Fun" button, the text of the header will change to "Welcome to the Club!" & the color of the paragraphs will change to red.
# ECMAScript
ECMAScript is the standard that JavaScript is based on.

Its purpose is to help JavaScript (& other languages) maintain compatibility across different runtimes. ECMAScript versions are released yearly, & they have a big impact on how we write modern JavaScript. Some notable versions include:
 * 2009: ECMAScript 5 (ES5) introduced `strict mode` & JSON support
 * 2015: ECMAScript 6 (ES6) introduced `let` & `const` for variable declarations
 * 2017: ECMAScript 8 (ES8) introduced asnyc/await
# Polyfills & Transpilers
Most programming languages change over time. The update from Python 2 to 3 is a famous example of an insane amount of breaking changes that caused many issues for Python Developers.

JavaScript has also changed over the years, but the interesting thing about being a language that primarily runs in the browser is that _you don't always control the runtime._ If you're running Python (or JS, on anything) on a _server_, then you can update your code, & at the same time update your runtime, compiler, or interpreter. With frontend JavaScript, you're at the mercy of whatever mix of out-of-date browsers your users are running.

Enter **polyfills & transpilers**.

A [polyfill](https://en.wikipedia.org/wiki/Polyfill_(programming)) is an extra bit of code you include to add functionality that some browsers might not support. For example, maybe Chrome allows you to use the fancy new `Array.prototype.flat()` method, but Internet Explorer 11 doesn't. You can include a polyfill (just some extra JavaScript code) that adds that method to the `Array` prototype so that your code works in both browsers.

A [transpiler](https://en.wikipedia.org/wiki/Source-to-source_compiler) (in the context of adding new JavaScript features) is basically a polyfill on steroids. Instead of just adding a method here or a property there, a transpiler will take your _entire_ JavaScript file & convert it into an older version of JavaScript that is known to work in all browsers. For example, it might take your fancy `async` & `await` keywords & convert them into a bunch of `Promise` objects & `.then()` calls. [Babel](https://babeljs.io/) is the most common transpiler for JavaScript.
# Modules
Back in the earliest days of JavaScript - when it was but a wee browser-only language that looked like bastardized Java - JavaScript files were _small_. A callback here, a dynamic element there, and a sprinkle of (gasp) [jQuery](https://jquery.com/) to make it all work.

But as the web has grown, we're not just shipping a bit of interactivity to static HTML pages anymore. We're building full-fledged applications with crazy amounts of state, logic, and dependencies. In the case of [single page applications](https://en.wikipedia.org/wiki/Single-page_application), sometimes HTML is just a shell that gets filled in with JavaScript at runtime.

Long story short, JS needed modules. In Go, you have packages. In Python, you have modules. Now, JavaScript also has modules - they're just a way to split your code into separate files and import the code you need across a large codebase.

**Modules in JavaScript exist at the file level**, just like Python. So, if you have a file called `math.js` that looks like this:
```js
// math.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = {
  add,
  subtract,
};
```
You can import & use those functions in another file like this:
```js
// main.js
const { add, subtract } = require("./math.js");

console.log(add(1, 2)); // 3
console.log(subtract(1, 2)); // -1
```
>[!NOTE]
> This is [CommonJS](https://en.wikipedia.org/wiki/CommonJS) syntax

# CommonJS
So we've started with the _less_ preferred way of doing modules in JavaScript: [CommonJS](https://en.wikipedia.org/wiki/CommonJS). CommonJS is a module system that was created for Node.js _before_ the new [ES6 module syntax](https://nodejs.org/api/esm.html#modules-ecmascript-modules) was introduced. It's still used in Node.js today, but ever since Node added support for ES6 modules, it's become less **common**.

CommonJS is Node.js specific, you can't use it in the browser without some kind of bundler. The defining features of CommonJS are:

* The [`module.exports`](https://nodejs.org/api/modules.html#modules_module_exports) object, which is used to export stuff
* The [`require`](https://nodejs.org/api/modules.html#modules_require) function, which is used to import stuff

## Exporting
```js
// math.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

module.exports = {
 add,
 subtract,
};
```
## Importing
```js
// main.js
const { add, subtract } = require("./math.js");

console.log(add(1, 2)); // 3
console.log(subtract(1, 2)); // -1
```
# Strict Mode
JavaScript is a loosey-goosey language. As such, it's easy to make mistakes that are hard to catch until you get a bug report.

[Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) is a way to opt-in to a more restrictive set of rules that help you catch errors earlier. It was introduced in ES5. Some of the big differences between strict mode & "normal" JavaScript are:

 * Eliminates some silent errors by throwing them
 * Fixes some mistakes that make it difficult for JS engines to optimize code. Strict mode code can sometimes run faster than identical code that's not in strict mode.
 * Prohibits some syntax likely to be defined in future versions of ECMAScript
 * `this` is `undefined` inside a function that's called without an object, instead of being the global object

Long story short, when possible, **strict mode is a good idea**.

To enable strict mode, you just need to "use strict" at the top of your file:
```js
"use strict";
// code
```
You _con_ also enable strict mode for a single function:
```js
function strictFunction() {
 "use strict";
 // code
}
```
## Strict Mode in Modules
Here's the best part: you only need `"use strict";` at the top of non-es6 modules. ES6 modules are always in strict mode by default. That goes for the browser & Node.js

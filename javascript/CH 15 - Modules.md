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

# ES6 Modules

ES6 modules are the preferred way of doing modules in JavaScript. They're (now) built into the language and are supported in modern browsers and Node.js. That said, there are still some [gotchas](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) to be aware of... which we'll cover.

## The Syntax

The syntax for ES6 modules is drop-dead simple. You can export stuff from a module using the [`export`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export) keyword, and import stuff using the [`import`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) keyword. Let's look at our math example again:

## Exporting
```js
// math.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
```

## Importing
```js
// main.js
import { add, subtract } from "./math.js";

console.log(add(1, 2)); // 3
console.log(subtract(1, 2)); // -1
```
# Node.js Modules
By default, Node.js uses the CommonJS syntax for modules. There are two ways you can manually switch to ES6 module syntax:

  1. Add `"type": "module"` to the top-level object in your `package.js` file
  2. Rename your module to `.mjs` instead of `.js`

The first option is cleaner & easier to manage. But remember, if you're not using ES6 modules, your code will _not_ be in strict mode by default!

# Browser Modules
Modern browsers now support ES6 modules, but there are a few things to be aware of. If you HTML has "normal" old script tags, those scripts will _not_ be treated as modules. They will execute one after the other, in the order they appear in the HTML file.
```html
<script src="meFirst.js"></script>
<script src="meSecond.js"></script>
```
If you want to use ES6 modules, you need to use the `type="module"` attribute on your script tags.
```html
<script type="module" src="meFirst.js"></script>
<script type="module" src="meSecond.js"></script>
```
Modules have a few great advantages:
  * Stuff defined in a module is _not_ in the global scope. To be accessed from another module, it must be exported.
  * Modules are deferred by default, meaning they only run after the document has been parsed.
  * Strict mode is enable by default.

# Default Exports

Default exports are often used when you want to export a _single value_ from a module.
```js
// math.js

export const add = (a, b) => a + b;
export const subtrackt = (a, b) => a - b;
```
```js
// main.js

import { add, subtract } from "./math.js";
```
This exports _two_ functions. Sometimes a dev may want to just export one thing, instead they can do this:
```js
// math.js

const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

export default add;
```
Then when it's imported, you don't need to use {} syntax:
```js
// main.js

import add from "./math.js"; // no curly braces
```
You can even have default _&_ named exports:
```js
// math.js

export const subtract = (a, b) => a - b; // named export

const add = (a, b) => a + b;
export default add; // default export
```
(You typically wouldn't do this)
## Should I use Default Exports?
You can, but what if you want to export more things later? Now you have to refactor all of your imports & exports. It's a pain.

# Bundlers

[Bundlers](https://webpack.js.org/concepts/) are tools that allow you to _write_ code in a modular & easy-to-manage way, and then _bundle_ it in a way that's optimized for production. For example, you probably want a giant front-end application to exist in your codebase as many hundreds of files, but you want to serve it to your visitors as a single file or one file per page.

The point is, a bundler takes care of transforming your code from _how you're writing it_ to _how you want it to be served._ That said, popular bundlers often do a whole suite of important things, like:

  * **Bundling**: Thus the name
  * **Minification:** Making your code smaller by removing unnecessary whitespace (useful when you have to serve your code to a browser via a slow connection)
  * **Code Splitting:** Breaking your code into smaller chunks that can be loaded on demand.
  * **Tree Shaking:** Removing unused code from your final bundle.
  * **Asset Optimization:** Optimizing images, fonts, & other assets i.e. converting images to WebP format or reducing their size.
  * **Source Maps:** Building files that allow you to debug your code in the browser as if it were still in its original form.

For a long time, [Webpack](https://webpack.js.org/) was the most popular bundler. It's still used, but [Vite](https://vitejs.dev/) has been gaining a lot of traction lately. Vite is often quite a bit faster than Webpack, & it's seemingly much easier to configure. It's built on top of (and adds more features to) [Rollup](https://rollupjs.org/), which is another popular bundler.

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
```js

# Basic Variables

The [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var) keyword declares a variable:
```js
var mySkillIssues = 42;
```

Some of JavaScript's most common variable types are:
* `number`: represents both int and float
* `boolean`: `true` or `false`
* `string`: a sequence of characters 
* `undefined`: a variable that hasn't been assigned a value

```js
var smsSendingLimit = 100;
var isAdmin = true;
var username = "wagslane";
var nothing = undefined;
```

### Assignment
* set the `username` variable to the value `"eddie_cabot"`

```js
// End of lesson code
var username = "eddie_cabot";
var isAdmin = true;
var smsSendingLimit = 100;
var costPerSMS = 0.05;

// don't touch below this line
console.log("username:", username);
console.log("isAdmin:", isAdmin);
console.log("smsSendingLimit:", smsSendingLimit);
console.log("costPerSMS:", costPerSMS);
```
# let and const

The `var` keyword is the "old" way to declare variables in JavaScript. These days, you should use [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) instead. The`let` keyword is for variables that can be reassigned, while `const` is for variables that can't.
```js
let username = "dengar_the_bh";
username = "boba_fett";

const smsSendingLimit = 1000;
```
Use `const` for values that never change, and `let` for values that do.

>[!WARNING]
>The `var` keyword is function-scoped instead of block-scoped, meaning when it's used inside an `if` block the variable leaks out, while `let` and `const` don't.
>You'll encounter legacy code that uses `var`, so you need to know about it, but migrate it to `let` or `const` when you can.

### Assignment
* Fix the double birfday message bug by changing the `var` keywords to `let` or `const` as appropriate
```js
// End of lesson code

let messageText = "Welcome to Textio!";
const isBirthday = true;

if (isBirthday) {
  let messageText = "Happy Birthday!";

  console.log("Sending birthday message...");
  console.log("Message:", messageText);
}

// don't touch below this line

console.log("Sending welcome message...");
console.log("Message:", messageText);
```
# Why JavaScript
[Video Notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/why-js-1920x1080.mp4)

Here's the deal, JavaScript is the _only_ language that runs in the browser. (There's [webassembly](https://webassembly.org/) but that's different). If you app is accessed via a web browser, it's almost certainly gonna need some JavaScript.

JavaScript has some things people don't like:
* Not statically typed (although TypeScript helps)
* Legacy baggage (like `var` and old code that doesn't use [promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise))
* Weird quirks like (`==` vs `===`)
* Always acts slightly differently in every browser/runtime

But it has some things going for it:
* Almost every technology uses it somehow, is there are a lot of jobs
* C-style syntax, so it's easy to learn if you know any other C-style language
* Many built-in features that are particularly useful on the web
* Can be used for both front-end & back-end development, simplifying an org's tech stack
* Big companies have invested a lot in making it better and faster over the years
* Great support for asynchronus programming

# Comments
JavaScript has two style of comments:
```js
// This is a single line comment

/*
This is a multi-line comment
*/
```
### Assignment
* Fix the syntax so the comments do not include the code
```js
// End of lesson code
// Attention!
/*
  We are increasing the maximum message length from 140 to 280 characters.
  Very reluctantly, I might add.
  Users actually want to write more than 140 characters?!? Madness.
*/

const maxMessageLength = 140;
const newMaxMessageLength = 280;
console.log(
  `Textio is increasing the maximum message length from ${maxMessageLength} to ${newMaxMessageLength} characters.`,
);
```

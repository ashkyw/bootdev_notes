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

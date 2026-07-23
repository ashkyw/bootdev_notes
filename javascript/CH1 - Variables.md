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
# Numbers in JS

In Python, numbers without a decimal point are called integers (`int`) and fractions are (`float`). Contrast this to JavaScript where all numbers are just a [`Number`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) type.

You're already familiar with the `number` type. Numbers aren't surrounded by quotes when created, but they can contain decimal parts and negative signs.
```js
let x = 2; // this is a number
x = 5.69; // this is also a number
x = -5.42; // yup, still a number
```
You can do arithmetic as you'd expect:
```js
let sum = 2 + 3 + 7; // 12
let difference = 5.3 - 2.1; // 3.2
let product = 2 * 3; // 6
let quotient = 6 / 2; // 3
```

### Assignment
Textio tracks the number of messages sent for different types of notifications. Between the comments, create a:
* `totalMessagesSent` variable that contains the total number of messages sent
* `averageMessagesSent` variable that contains the average number of messages sent across all types.
```js
// End of lesson code
const promoMessages = 12;
const reminderMessages = 15;
const welcomeMessages = 8;
const supportMessages = 5;

// don't touch above this line

const totalMessagesSent =
  promoMessages + reminderMessages + welcomeMessages + supportMessages;
const averageMessagesSent = totalMessagesSent / 4;

// don't touch below this line

console.log("Total messages:", totalMessagesSent);
console.log("Average messages:", averageMessagesSent);
```
# Increment & Decrement

In Python we use the `+=` operator to increment a number. That operator works in JavaScript as well, but JS also has a [`++` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment) for when you only want to increment by `1`.

```js
let bootdevCourseRating = 4;
bootdevCourseRating++;
console.log(bootdevCourseRating); // 5
bootdevCourseRating += 5;
console.log(bootdevCourseRating); // 10
```

And of course, there is a [`--` operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Decrement) for decrementing by `1`

```js
let bootdevCourseRating = 11;
bootdevCourseRating--;
console.log(bootdevCourseRating); // 10
bootdevCourseRating -= 5;
console.log(bootdevCourseRating); // 5
```

### Assignment
* Use the `++` operator to increment the `numFailedMessages`
```js
// End of lesson code
let numFailedMessages = 1336;
numFailedMessages++;
console.log(numFailedMessages + " failed messages");
```
# Undefined vs. Undeclared

The primitive [`undefined`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) value represents the absence of a value... but it's not the same thing as an "undeclared" variable!

We can create an _undefined_ variable by giving it a name, but no value:
```js
let favoriteSandersonCharacter; // undefined
console.log(typeof favoriteSandersonCharacter); // "undefined"
```
However if we _never create the name_, it's "undeclared", and undeclared variables actually throw an error (so don't do this):
```js
console.log(favoriteRothfussCharacter); // ReferenceError: favoriteRothfussCharacter is not defined
```
The worst part is that the undeclared variable error actually says "not defined"... Welcome to JavaScript
> [!NOTE]
> As an aside, you can use `const` to declare a variable that is assigned to `undefined`,but you wouldn't be able to set its value later, so why would you want to? 
```js
const favoriteSandersonCharacter; // SyntaxError: missing = in const declaration
const favoriteSandersonCharacter = undefined; // undefined
```
### Assignment
Create the missing variables used in the `console.log` calls so that they are declared but `undefined`
```js
// End of lesson code
let sentMessages;
let deliveredMessages;
let failedMessages;

// don't touch below this line

console.log("Sent is:", sentMessages);
console.log("Delivered is:", deliveredMessages);
console.log("Failed is:", failedMessages);
```
# Null vs. Undefined
If you're coming from Python, you might be thinking:
> Ahh, so `undefined` is like `None`! Easy.

Yes. But also... no. One of JavaScript's most cursed features is that it has two values for "nothing":
* `undefined`: It doesn't exist _at all_. In grug-speak `undefined` is "very nothing"
* `null`: It (kind of) exists, but it's _empty_. In grug_speak `null` is "kinda nothing"

There are [some practical differences between the two](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/null#difference_between_null_and_undefined), the primary one being that `undefined` is the _default_ value of a variable when it hasn't been given a value yet.
```js
let myName;
console.log(myName); // undefined
```
To get a `null` value, you have to explicitly assign it:
```js
let myName = null;
console.log(myName); // null
```
Confusingly, `typeof` returns `"object"` for `null`:
```js
console.log(typeof null); // object
```
_To be clear, `null` **is** its own type according to [ECMAScript specification](https://tc39.es/ecma262/#sec-ecmascript-language-types), but the "object" type report is a historical quirk that [can't be easily fixed now](https://web.archive.org/web/20071020084354/http://wiki.ecmascript.org/doku.php?id=proposals%3Atypeof)_

In _most cases_, `null` and `undefined` work the same way, but you'll want to be consistent in _how_ you use them, and know thah there are subtel behavioral differences.

> use `undefined` everywhere you would use `None` in Python. JavaScript is fairly unique in having two options. Use `null` in cases where the behavioral difference matters, or external code forces the use of`null`

### Assignment
Fix the code so eakh variable holds a `null` value
```js
// End of lesson code
let sentMessages = null;
let deliveredMessages = null;
let failedMessages = null;

// don't touch below this line

console.log("Sent is null:", sentMessages === null);
console.log("Delivered is null:", deliveredMessages === null);
console.log("Failed is null:", failedMessages === null);
```
# Dynamic & Weak
Like Python, Ruby, and PHP, JavaScript is a dynamically-type (not statically-typed) language. Its variable types are only known at _runtime_

_Unlike_ Python, it's also [weakly typed](https://en.wikipedia.org/wiki/Strong_and_weak_typing) meaning it will automatically convert types when you do things like add a number to a string. This can lead to some unexpected behavior if you're not careful...
```js
let answerToLife =  42;
let answerToTheUniverse = "42";
// obviously JavaScript think that adding strings
// and number is totally sane and normal behavior
const answerToEverything= answerToLife + answerToTheUniverse;

console.log(answerToEverything);
//"4242"
```
### Assignment
Fix the error by ensuring the value matches the correct type as you'd expect.
```js
let totalSentMessages = 100;
let totalReceivedMessages = 50;

// don't touch below this line

const totalMessages = totalSentMessages + totalReceivedMessages;

console.log("Total sent messages:", totalSentMessages);
console.log("Total received messages:", totalReceivedMessages);
console.log("Total messages:", totalMessages);
```
# Same line declarations

You can declare multiple variables on the same line:
```js
let miles = 80276, org = "Tesla;"
```
The above is the same as:
```js
let miles = 80276;
let org = "Tesla";
```
### Assignment
Declare `averageOpenRate` and `displayMessage` in the same `const` declaration.
Initialize them to values (num and str):
* `0.23`
* `is the average open rate of your messages`

```js
// End of lesson code
const averageOpenRate = 0.23,
  displayMessage = "is the average open rate of your messages";

// don't touch below this line

console.log("Average open rate:", averageOpenRate);
console.log("Display message:", displayMessage);
```
# JavaScript's Speed
Comparing the "speed" or "efficiency" of programming languages is far from an exact science. There are a lot of variables and moving parts so benchmarks can be misleading. 

A few high-level things to provide a frame-of-reference:
* JavaScript is not as fast as C, Rust or Zig. It's almost always going to be outperformed by non-garbage-collected languages
* Modern JavaScript is typically JIT-compiled into machine code via the [V8 Engine](https://v8.dev/) at runtime. It's usually not as fast as AOT (ahead-of-time) compiled languages like Go or C, put it's usually much faster than interpreted languages like Python or Ruby
* JavaScript runs on a single threa, but has greater support for asynchronous programming, It's typically not as performant for CPU-bound tasks (like heavy math calculations), but it does well for I/O-bound tasks (like contacting a database or making an API call).

# Strings

In JavaScript, a (non-template) string can be written with either single or double quotes. For example:
*`'Hello'`
*`"Hello"`

**Double quotes are preferred**. It's important to have styling conventions so that all the code in a project looks consistent, making it easier to read and contribute to.

## Indexing

Square brackets are used to access individual characters inside a string. The characters are numbered from `0` to `length-1`. It's similar to how strings and lists work in Python & many other languages.
```js
const greeting = "Hello";
console.log(greeting[0]); // 'H'
console.log(greeting[1]); // 'e'
console.log(greeting[2]); // 'l'
console.log(greeting[3]); // 'l'
console.log(greeting[4]); // '0'
// you can also get the last char at length-1
console.log(greeting[greeting.length-1]); // 'o'
```
The [`.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length) property is used to get the number of characters in a string.

### Assignment
Print some characters
```js
// End of lesson code
const email = "stoob@boot.dev";

// print the first character in the string here
console.log(email[0]);

// print the last character in the string here
console.log(email[email.length - 1]);

// print the entire string here
console.log(email);
```
# Template Literals

In JavaScript [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) are a fantastic way to interpolate dynamic values into a string. They're JavaScript's version of Python's f-strings. For example:
```js
const shadeOfRed = 101;
console.log(`The shade is ${shadeOfRed}`);
// The shade is 101
```
Template literals _must start and end with a backtick_, and anything inside of the dollar-sign bracket enclosure is automaticallly _cast_ to a string.

t## Advanced Logic
You aren't limited to just variable names inside the `${}`. You can actually write valid JavaScript code directly inside them. 
This means you can do math, change text styles, or run logic checks right inside the string.
```js
const price = 2.5;
const quantity = 3;
const item = "coffee";

console.log(`Total: $${price * quantity}`);
// Total: $7.5

console.log(`I need ${item.toUpperCase()}`);
// I need COFFEE
```
### Assignment
Using template literals and string formatting, create a new variable `msg` and assign it to the string:
```
HI NAME, your open rate is OPENRATE percent
```

```js
// End of lesson code
const name = "Saul Goodman";
const openRate = 30.5;

const msg = `Hi ${name}, your open rate is ${openRate} percent`;

console.log(msg);
```
# Java vs. JavaScript
A _very_ common misconception is that Java and JavaScript are the same, or even just similar.
> Java is to JavaScript as car is to carpet

Java & JavaScript ore _not_ the same, and they often aren't even used for the same kinds on things.

## Java
[Java](https://www.java.com/en/) is a statically-typed, object-oriented language that compiles to byte code and runs on the Java Virtual Machine. It's used fore all sorts of things, but most commonly for server-side applications, Android apps, and large entreprise systems.

## JavaScript
JavaScript is a dynamically and weakly-typed language that runs natively in the browser and out of the browser with dedicated runtimes like Node.js, Deno, or Bun. It originally _only_ ran in the browser and was named "JavaScript" because back when it was created in the 90's, Java was _very_ popular and the creators wanted to get a piece of that marketing.

## Fun Fact
[Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich), the creator of JavaScript, was given only 10 days to create the language. He was told to make it look like Java, but to make it work in the browser.

# Semi-colon in JS

In languages like C, C++ and Java, a semicolon is used as a statement terminator. For example, in C:
```c
int x = 5;
```
This allows the compiler to know when a statement ends without relying on whitespace or newlines. For example, this is also valid C:
```c
int x = 5; int y = 10;
```
In JavaScript, semicolons are _optional_ as a terminating character. They can be inserted by the JavaScript engine automatically during the parsing phase. However, most developers prefer to use semi-colons to avoid any confusion or errors that can arise from automatic insertion
```js
// This works
let x = 5
let y = 10
```
```js
// But this is preferred
let x = 5;
let y = 10;
```
### Assignment
```js
// End of lesson code
console.log("contacting cell tower..."); console.log("sending message...");
// don't go past line 1 with your code
```

# Functions

JavaScript supports functions via the `function` keyword
```js
// function declaration
function getSum(a, b) {
  return a + b;
}

// function call
const result = getSum(60, 9);

console.log(result);
// 69
```
### Assignment
```js
// End of lesson code
function concat(str1, str2) {
  return str1 + str2;
}

// don't touch below this line

console.log(concat("Lane,", " happy birthday!"));
console.log(concat("Naomi,", " can you call me?"));
console.log(concat("Juliette,", " where did you go?"));
```
#  Function Hoisting
In Python a function must be defined _before_ any code that executes it. In JavaScript, functions simply need to be defined**_somewhere_** in the file. Functions can be called even _before_ it's definition.
```js
console.log(getLabel(3));
// prints 'awful'

function getLabel(numStars) {
  if (numStars > 7) {
    return "great";
  } else if (numStars > 3) {
    return "okay";
  } else {
    return "awful";
  }
}
```
This works because JavaScript ["hoists"](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting) the function declaration to the top of the file _before_ the code is executed.

# Multiple Return Values
Many languages allow multiple values to be returned from a function. For example, in Python:
```py
def get_user():
  return "name@domain.com", 21, "active"

email, age, status = get_user()
```
However in JavaScript, that's _not allowed!_
```js
function getUser() {
  return "name@domain.com", 21, "active";
// DON'T DO THIS!!
// it only returns 'active'
}
```
Strangely, the JavaScript code above won't actually _throw_ any sort of error, it will silently return the `"active"` string... which is unintuitive behavior that you probably didn't want. **You can only return one value from a function in JavaScript**

To get around this, most devs return an object that _contains_ the values they want to return. **More on objects later.**

### Assignment

Fix the `isClean` function.

```js
function isClean(review) {
  let clean = true;
  if (review.includes("dang")) {
    clean = false;
  }
  if (review.includes("shoot")) {
    clean = false;
  }
  if (review.includes("heck")) {
    clean = false;
  }
  return clean;
}

// don't touch below this line

export { isClean };
```
# Functions as Values
JavaScript supports [first-class]() & higher-order functions, which are just fancy ways of saying "functions as values". Functions can be treated like any other data type -- such as `number`s & `string`s & `boolean`s. Let's assume we have two simple functions:
```js
function add(x, y) {
  return x + y;
}

function mul(x, y) {
  return x * y;
}
```
We can create a new `aggregate` function that accepts a function as its 4th arguemnt
```js
function aggregate(a, b, c, arithmetic) {
  const firstResult = arithmetic(a, b);
  const secondResult = arithmetic(firstResult, c);
  return secondResult;
}
```
It calls the given `arithmetic` function (which could `add` or `mul`, or any other function that accepts two parameters & returns a number) and applies it to three inputs instead of two. It can be used like this:
```js
function main() {
  const sum = aggregate(2, 3, 4, add);
  // sum is 9
  const product = aggregate(2, 3, 4, mul);
  // product is 24
}
```
### Assignment
* Apply the given `formatter` _three times_ to the `message`
* Add a prefix of `TEXTID: ` to the result
* return string

```js
function reformat(message, formatter) {
  let formattedMessage = formatter(formatter(formatter(message)));
  return `TEXTIO: ${formattedMessage}`;
}

// don't touch below this line

export { reformat };

```
# Scope
[Scope](https://developer.mozilla.org/en-US/docs/Glossary/Scope) in JavaScript defines where variables and functions are accessible in your code, and it can behave differently depending on the environment (such as a browser or Node.js). There are four levels, from highest to lowest:
1. Global Scope:
   * Variables declared globally have the highest level of scope and can be accessed from anywhere in the code
   * In browsers, global variables are properties of the `window` object. For example, `window.myGlobalVar = 'hello world'` defines a global variable.
   * In Node.js, global variables are properties of the `global` object: `global.myGlobalVar = 'hello world'`

2. Module Scope:
   * In ES modules (both in Node.js & modern browsers), variables declared at the top level of a module are scoped to that module. They are not added to the global scope.
   * In browser, using `<script type="module">` creates a module scope for that script.

3. Function Scope:
   * variables declared with `var` are limited to the function scope. They are only accessible within that function & nested functions.

4. Block Scope:
  * [ES6](https://en.wikipedia.org/wiki/ECMAScript) introduced block scope with the `let` and `const` keywords. A block is typically defined by curly braces `{}`, like in `if` statements & other blocks of code.
  * Variables declared with `let` & `const` are confined to their block, making them more predictable & reducing the chances of accidental variable hoisting.

### Assignment
Fix `getMessageStatus`

```js
function getMessageStatus(message) {
  let messageStatus = "processing";

  function isValidLength(message) {
    let messageStatus = "invalid";

    if (message.length > 0) {
      messageStatus = "valid";
    }

    return messageStatus;
  }

  // don't touch above this line

  messageStatus = isValidLength(message);
  return messageStatus;
}

// don't touch below this line

export { getMessageStatus };

```
# Anonymous Functions
Anonymous Functions are true to form in that they have _no name_. They're useful when defining a function that will only be used once or to create a quick [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)).

Let's say we have a function `conversions` that accepts another function, `converter` as input:
```js
function conversions(converter, x, y, z) {
  const convertedX = converter(x);
  const convertedY = converter(Y);
  const convertedZ = converter(z);
  console.log(convertedX, convertedY, convertedZ);
}
```
We _could_ define a function normally and then pass it in by name... but if we only want to use it in this one place, we can define it inline as an anonymous function:
```js
// using a named function
function double(a) {
  return a + a;
}
conversions(double, 1, 2, 3);
// 2 4 6
```
```js
// using an anonymous function
conversions(
  function (a) {
    return a + a;
  },
  1,
  2,
  3,
);
// 2 4 6
```
### Assignment
Complete `printReports`:
1. For each call to `printCostReport` pass:
  * an anonymous function that calculates the cost of a message as an integer
  * the message itself

2. The cost for each type of message is calculated like this:
   Intro: 2x the message length
   Body: 3x the message length
   Outro: 4x the message length

Use the built-in `length` property to get the length of a string:
```js
const helloLen = "hello".length;
// helloLen = 5
```
     
```js
// End of lesson code
function printReports(intro, body, outro) {
  printCostReport(function (msg) {
    return msg.length * 2;
  }, intro);
  printCostReport(function (msg) {
    return msg.length * 3;
  }, body);
  printCostReport(function (msg) {
    return msg.length * 4;
  }, outro);
}

// don't touch below this line

function printCostReport(costCalculator, message) {
  const cost = costCalculator(message);
  console.log(`Message: "${message}" Cost: ${cost} cents`);
}

printReports(
  "Welcome to the Hotel California",
  "Such a lovely place",
  "Plenty of room at the Hotel California",
);

```
# Default Parameters
In JavaScript, you can specify default values for function parameters. This is particularly useful for _optional_ parameters where you want to ensure a specific default behavior if the caller does not provide certain arguments. Default parameter values can be set during the function declaration.
```js
function getGreeting(email, name = "there") {
  console.log(`Hello ${name}, welcome! You've registered your email: ${email}`);
}
getGreeting("lane@example.com", "Lane");
// Hello Lane, welcome! You've registered your email lane@example.com

getGreeting("lane@example.com");
// Hello there, welcome! You've registered your email lane@example.com
```
If the second parameter is omitted the default `"there"` will be used in its place. Optionaal parameters (those with default values) should be defined after all mandatory parameters to avoid ambiguity.

### Assignment
Complete `createContact`, it takes three parameters:
* `phoneNumber`
* `name`, with a default parameter of `'Anonymous'`
* `avatar`, with a default parameter of  `'default.jpg'`

If a `phoneNumber` is not passed, return `"Invalid phone number`, otherwise concatenate the given `avatar` to the string "/public/pictures/".
Return a string in this format: 
`Contact saved! Name: NAME, Phone number: PHONE_NUMBER, Avatar: AVATAR_FILEPATH`
```js
function createContact(
  phoneNumber,
  name = "Anonymous",
  avatar = "default.jpg",
) {
  if (!phoneNumber) {
    return "Invalid phone number";
  }

  const avatarFilePath = "/public/pictures/" + avatar;

  return `Contact saved! Name: ${name}, Phone number: ${phoneNumber}, Avatar: ${avatarFilePath}`;
}

// don't touch below this line

export { createContact };

```
# Passing by Value
Variables in JavaScript are typically passed by value (except for objects, and arrays, which are passed by reference -- more to come on these). "Pass by value" means that when a variable is passed into a function, that function receives a copy of the variable. The function is unable to mutate the caller's original data.
```js
let x = 5;
increment(x);
console.log(x);
// 5

function increment(x) {
  x++;
  console.log(x);
  // 6
}
```
### Assignment
```js
function getBillForMonth(costPerSend, messagesSent) {
  return costPerSend * messagesSent;
}

function monthlyBillIncrease(costPerSend, numLastMonth, numThisMonth) {
  let lastMonthBill = getBillForMonth(costPerSend, numLastMonth);
  let thisMonthBill = getBillForMonth(costPerSend, numThisMonth);
  return thisMonthBill - lastMonthBill;
}

// don't touch below this line

export { getBillForMonth, monthlyBillIncrease };
```

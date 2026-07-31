# Conditionals

`if`  statements in JavaScript use parentheses around the condition:
```js
if (height > 4) {
  console.log("You are tall enough!");
}
```
`else if` and `else` are supported as you might expect:
```js
if (height > 6) {
  console.log("You are super tall!");
} else if (height > 4) {
  console.log("You are tall enough!");
} else {
  console.log("You are not tall enough!");
}
```
Common comparison operators:
* `===` equal to
* `!==` not equal to
* `<` less than
* `>` greater then
* `<=` less than or equal to
* `>=` greater than or equal to

### Assignment
Correct comparison operators:
```js
let messageLen = 10;
let maxMessageLen = 20;
console.log(
  "Trying to send a message of length:",
  messageLen,
  "and a max length of:",
  maxMessageLen,
);

// don't touch above this line

if (messageLen <= maxMessageLen) {
  console.log("Message sent");
} else {
  console.log("Message not sent");
}
```

# Comparison Operators
These inequality operators work as you expect in JavaScript:
```js
5 < 6; // true
5 > 6; // false
5 >= 6; // false
5 <= 6; // true
```
The [equality operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness), however, are a bit... _strange_. To compare two values to see if they are _exactly_ the same, use the [strict equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality) (`===`) and [strict inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_inequality) (`!==`) operators:
```js
5 == 6; // false
5 !== 6; // true
```
The "normal" [equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality) (`==`) and [inequality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Inequality) (`!=`) operators are a bit more _flexible_:
```js
5 == 6; // false
5 == "5"; // true

5 != 6; // true
5 != "5"; // false
```
The "strict equals" (`===`) and "strict not equals" (`!==`) compare both the value _and_ the type. The "loose equals" (`==`) and "loose not equals"  (`!=`) attempt to convert and compare values of different types. With the loose versions, the string `'5'` and the number `5` are considered "equal", which, in _good_ code, is usually _not_ what you want.

**This is a fairly unique quirk of the JavaScript language**.

You can [read more about how `==` works](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Equality#description) if you're interested, but I'd recommend sticking with `===` and `!==` in nearly all cases.

# Logical Operators
In JavaScript, the equivalent logical operators use symbols:
* `&&` (and)  - Returns `true` if _both_ conditions are `true`
* `||` (or) - Returns `true` if _either_ of the conditions are `true`
* `|` (not) - Returns `true` only if the input is `false`
```js
true && true; // true
true && false; // false
true || false; // true
false || false; // false
!false; // true
!true; // false
```
_This syntax matches other languages like Go, Rust, & C_

### Assignment
Set `isHighEngagement` using logical operators:
```js
const hasHighOpenRate = true;
const isRecent = true;
const hasStrongReplyRate = false;
const canBeResent = true;
const isFlaggedAsSpam = false;

// don't touch above this line

const isHighEngagement =
  hasHighOpenRate &&
  isRecent &&
  (hasStrongReplyRate || canBeResent) &&
  !isFlaggedAsSpam;

// don't touch below this line

console.log(`The campaign is high-engagement: ${isHighEngagement}`);
```
# Switch
[Switch statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch) are a way to compare a variable against multiple possible values. They are similar to if-else statements, but tend to be more readable when there are many potential options.
```js
const os = "mac";
let creator;
switch (os) {
  case "linux":
    creator = "Linus Torvalds"
    break;
  case "windows":
    creator = "Bill Gates"
    break;
  case "mac":
    creator = "Steve"
    break;
  default
    creator = "Unknown"
    break;
}

console.log(creator);
// Steve
```
Unlike some languages where fall-through doesn't happen by default, JavaScript **will continue** to execute the next case until it reaches a `break` or `return` statement.

_99 times out of 100, you'll want to include a `break/return` statement after each case to prevent this behavior_

### Assignment
Set the "pro" and "enterprise" plans correctly:
* pro: `20.0`
* enterprise: `50.0`
```js
function billingCost(plan) {
  switch (plan) {
    case "basic":
      return 10.0;
    case "pro":
      return 20.0;
    case "enterprise":
      return 50.0;
    default:
      return 0.0;
  }
}

// don't touch below this line

console.log(`The cost for a basic plan is $${billingCost("basic").toFixed(2)}`);
console.log(`The cost for a pro plan is $${billingCost("pro").toFixed(2)}`);
console.log(
  `The cost for a enterprise plan is $${billingCost("enterprise").toFixed(2)}`,
);
console.log(`The cost for a free plan is $${billingCost("free").toFixed(2)}`);
console.log(
  `The cost for a unknown plan is $${billingCost("unknown").toFixed(2)}`,
);

```
# Ternary Operator

Sometimes using 3-5 lines of code to write an if/else block is overkill. The [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator) makes it easy to write a conditional as a single [expression](https://en.wikipedia.org/wiki/Expression_(computer_science)).
```js
const price = isMember ? "2.00" : "10.00";
```
 Can be read in plain English as:
 > If `isMember` is true, evaluate to `$2.00`, otherwise evaluate to `$10.00`.

The same logic using if/else would be:
```js
let price;
if (isMember) {
  price = "$2.00";
} else {
  price = "$10.00";
}
```
## Why is it called a "Ternary"?
Ternary's Latin root means "3", and it's the only JavaScript operator that takes _three_ operands.
* A condition followed by a question mark (?)
* An expression to execute if the condition is truthy followed by a colon (`:`)
* The expression to execute if the condition is falsy.

### Assignment
Create variable `messageStatus` and use a ternary operator to set the value to either:
* `"Processing"`: the number of retries is less than the limit
* `"Failed"`: the number of retries is greater than or equal to the limit
```js
// End of lesson code
const retryLimit = 10;
const numRetries = 9;

// don't touch above this line

const messageStatus = numRetries < retryLimit ? "Processing" : "Failed";

// don't touch below this line

console.log(messageStatus);
```
# When to Ternary

Most often you will be using if/else statements more than ternaries. Ternary operators are great for _small_, single-line conditionals. Developers in the professional world can get... _clever_... with ternaries and it can lead to nested monstrosities like this:
```js
const vehicleName = isTruck
  ? "truck"
  : isCar
    ? "car"
    : isScooter
    ? "scooter"
    : "vehicle";
```
It _works_ & it's all on one line, but it's much harder to understand. This is generally preferred:
```js
let vehicleName = "vehicle";
if (isTruck) {
  vehicleName = "truck";
} else if (isCar) {
  vehicleName = "car";
} else if (isScooter) {
  vehicleName = "scooter";
}
```
or maybe a function:
```js
function getVehicleName(isTruck, isCar, isScooter) {
  if (isTruck) {
    return "truck";
  }
  if (isCar) {
    return "car";
  }
  if (isScooter) {
    return "scooter";
  }
  return "vehicle";
}
```
Remember: **Code is written for _humans_** not machines.

# Truthy & Falsy
A ["truthy"](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) value is a value that is considered `true` when encountered in a Boolean context. In JavaScript, you don't _need_ to explicitly convert a value to a Boolean before using it in a conditional:
```js
if ("hello") {
  console.log("hello is truthy");
}
if (42) {
  console.log("42 is truthy");
}
// hello is truthy
// 42 is truthy
```
A ["falsy"](https://developer.mozilla.org/en-US/docs/Glossary/Falsy), but for values that evaluate to `false`:
```js
if (!0) {
  console.log("0 is falsy");
}
if (!null) {
  console.log("null is falsy");
}
if (!undefined) {
  console.log("undefined is falsy");
}
```
Common truthy values include:
* `true`
* `42` (any number that isn't `0`)
* `"hello"` (any non-empty string) 
* `[]` (an empty array)
* `{}` (an empty object)
* `function() {}` an empty function

Common falsy values include:
* `false`
* `0`
* `""` (an empty string)
* `null`
* `undefined`
* `NaN`
* 
### Assignment
Fix a line for correct checks

```js
// End of lesson code
const userCredits = -2;

if (userCredits > 0) {
  console.log("Sending message...");
} else {
  console.log("Not enough credits.");
}
```

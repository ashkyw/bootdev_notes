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

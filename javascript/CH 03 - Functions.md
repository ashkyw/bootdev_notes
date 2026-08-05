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

```

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

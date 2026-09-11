# Arrays
JavaScript's [arrays]() are similar to Python's lists.

One important thing about JavaScript arrays is that items in an array are _not_ required to be of the same type. Remember: JavaScript is about as loosey-goosey as programming languages get.
```js
const numbers = [1, 2, 3, 4, 5];
const strings = ["banana", "apple", "pear"];
const miscellaneous = [true, 7, "adamantium"];
```
You can index into an array using `[]`:
```js
const strings = ["banana", "apple", "pear"];
console.log(strings[0]);
// Prints: 'banana'
```
And you can `.push()` new items onto the end of an array:
```js
const drinks = [];
drinks.push("lemonade");
console.log(drinks);
// Prints: ['lemonade']
drinks.push("root beer");
console.log(drinks)
// Prints: ['lemonade', 'root beer']
```
### Assignment
* Create `sentMessages` - an empty array
```js
const sentMessages = [];
sentMessages.push("Welcome to Textio!");
logArray(sentMessages);
sentMessages.push("Reminder: Your payment is due soon.");
logArray(sentMessages);

function logArray(arr) {
  console.log("Array contents:");
  for (const el of arr) {
    console.log(` - ${el}`);
  }
  console.log("=======================================");
}
```
# Array Length
The [`.length`]() _property_ returns the current length of an array.
```js
const foods = ["burger", "fries", "pizza"];
console.log(foods.length);
// Prints 3
```
### Assignment
Complete `getMostRecentUser`
```js
const getMostRecentUser = (usernames) => {
  if (usernames.length === 0) {
    return null;
  }
  return usernames[usernames.length - 1];
};

export { getMostRecentUser };
```
# Array Spread
Remember the [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) for merging object properties? **It works with arrays too**! It expands the elements of an array into individual elements & inserts them into another array.
```js
const nums = [1, 2, 3];
const newNums = [...nums, 4, 5, 6];
console.log(newNums);
// Prints: [1, 2, 3, 4, 5, 6]
```
### Assignment
Complete the `uploadNewMessages` function
```js
const uploadNewMessages = (oldMessages, newMessages) => {
  return [...oldMessages, ...newMessages];
};

export { uploadNewMessages };
```
# Includes
Checking whether a value exists in an array is really easy in JavaScript, just use the `.includes()`method.
```js
fruits = ["apple", "orange", "banana"];
console.log(fruits.includes("orange"));
// Prints: true
console.log(fruits.includes("pear"));
// Prints: false
```
Array `.includes()` checks exact elements; string `.includes()` checks substrings:
```js
const str = "Hello, world!";
console.log(str.includes("world"));
// Prints: true
console.log(str.includes("banana"));
// Prints: false
```
### Assignment
Complete the `getCleanRank` function
```js
function getCleanRank(reviewWords) {
  const hasDang = reviewWords.includes("dang");
  const hasShoot = reviewWords.includes("shoot");
  const hasHeck = reviewWords.includes("heck");

  let numWords = 0;
  if (hasDang) {
    numWords++;
  }
  if (hasShoot) {
    numWords++;
  }
  if (hasHeck) {
    numWords++;
  }

  if (numWords === 0) {
    return "clean";
  }
  if (numWords === 1) {
    return "dirty";
  }
  return "filthy";
}

export { getCleanRank };
```
# For...of Loops
JavaScript has a relatively new [`for...of`]()syntax to loop over a sequence without the need to keep track of the index manually. So, instead of typing out all of this:
```js
let woods = ["oak", "pine", "maple"];
for (let i = 0; i < woods.length; i++) {
  console.log(woods[i]);
}
// Prints:
// Oak
// Pine
// Maple
```
We can instead write this:
```js
let woods = ["oak", "pine", "maple"];
for (let wood of woods) {
  console.log(wood);
}
// Prints:
// Oak
// Pine
// Maple
```
It's a lot like Python's `for...in` syntax, but be careful not to confuse it with JavaScript's `for...in` syntax, which is used to loop over the _keys_ of an object.
### Assignment
Complete the `getCleanMessages` function
```js
const getCleanMessages = (messages, badWord) => {
  const loweredBadWord = badWord.toLowerCase();
  const cleanMessages = [];
  for (const message of messages) {
    const loweredMessage = message.toLowerCase();
    if (!loweredMessage.includes(loweredBadWord)) {
      cleanMessages.push(message);
    }
  }
  return cleanMessages;
};

export { getCleanMessages };
```

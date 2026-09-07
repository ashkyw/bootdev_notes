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

```

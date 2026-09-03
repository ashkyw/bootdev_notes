# Loops

A traditional "for loop" in JavaScript looks like this:
```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// 0
// 1
// 2
// 3
// 4
```

The syntax is common in C-style languages.

### Assignment
Complete the `bulkSendCost` function
```js
function bulkSendCost(numMessages) {
  let totalCost = 0.0;
  for (let i = 0; i < numMessages; i++) {
    totalCost += 1 + i * 0.01;
  }
  return totalCost;
}

export { bulkSendCost };
```

# Break
The [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break) keyword can be used to break out of a loop early.
```js
for (let i = 0; i < 10; i++ ){
  if (i === 3) {
    break;
  }
  console.log(i);
}
// Prints:
// 0
// 1
// 2
```
You can omit the loop condition in a `for` loop to create an intentional infinite loop and then use `break` to exit, for example:
```js
for (let i = 0; ;i++) {
  if (i === 3) {
    break;
  }
  console.log(i);
}
```
No matter the end condition, when a `break` statement is encountered, the loop exits immediately.
### Assignment
Complete the `maxMessagesWithinBudget` function
```js

```

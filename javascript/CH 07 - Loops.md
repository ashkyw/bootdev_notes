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
function maxMessagesWithinBudget(budget) {
  let totalCost = 0;
  let count = 0;

  for (let i = 0; ; i++) {
    const cost = 1.0 + i * 0.01;
    if (totalCost + cost > budget) {
      break;
    }
    totalCost += cost;
    count += 1;
  }

  return count;
}

export { maxMessagesWithinBudget };
```
# Continue
The [`continue`]() keyword stops the current iteration of a loop & immediately moves on the the next one.
```js
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}
// Prints:
// 1
// 3
// 5
// 7
// 9
```
### Assignment
Complete the **`printPrimes`** function:

```js
function printPrimes(max) {
  for (let n = 2; n <= max; n++) {
    if (n === 2) {
      console.log(n);
      continue;
    }
    if (n % 2 === 0) {
      continue;
    }
    let isPrime = true;
    for (let i = 3; i * i <= n; i += 2) {
      if (n % i === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      console.log(n);
    }
  }
}

function test(max) {
  console.log(`Primes up to ${max}:`);
  printPrimes(max);
  console.log(
    "===============================================================",
  );
}

test(10);
test(20);
test(30);
```

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
# While
Like many other langauages, JavaScript has a [`while`]() loop. It keeps running as long as the condition is true.
```js
const jane = {
  name: "Jane",
  mom: {
    name: "Alice",
    mom: {
      name: "Lilly",
      mom: {
        name: "Granny",
      },
    },
  },
};

let currentPerson = jane;
while (currentPerson) {
  console.log(currentPerson.name);
  currentPerson = currentPerson.mom;
}
console.log("No more ancestors!");
// Jane
// Alice
// Lilly
// Granny
// No more ancestors!
```
### Assignment
Fix the while loop.
```js
function getMaxMessagesToSend(costMultiplier, maxCostInPennies) {
  let actualCostInPennies = 1.0;
  let maxMessagesToSend = 1;
  let balance = maxCostInPennies - actualCostInPennies;
  while (balance > 0) {
    actualCostInPennies *= costMultiplier;
    balance -= actualCostInPennies;
    maxMessagesToSend++;
  }
  if (balance < 0) {
    maxMessagesToSend--;
  }
  return maxMessagesToSend;
}

export { getMaxMessagesToSend };
```
# For...in
Sometimes it's useful to loop over all the _keys_ of an object. This is _most_ useful when you're using an object as you would use a dictionary or hash map in other languages.
```js
let titan = {
  name: "Eren",
  power: "Attack Titan",
  age: 19,
};

for (const key in titan) {
  console.log(`${key}: ${titan[key]}`);
}

// name: Eren
// power: Attack Titan
// age: 19
```

In modern specifications, the traversal order is well-defined & consistent across implementations.
> Within each component of the prototype chain, all non-negative integer keys (those that can be array indices) will be traversed first in ascending order
> by value, then other string keys in ascending chronological order of property creation.

That is not necessarily obvious when reading code. It may be easier to break out the keys into an array & sort them how you want.
### Assignment
Complete the `printMatchinProperties` function.
```js
const printMatchingProperties = (messageLog, searchTerm) => {
  for (const key in messageLog) {
    if (key.startsWith(searchTerm)) {
      console.log(`Found: ${key} -> ${messageLog[key]}`);
    }
  }
};

// don't touch below this line

const messageLogs = [
  {
    messageId: "abc123",
    messageText: "Your order has shipped",
    timestamp: "2025-02-06T12:34:56Z",
    sender: "TextioBot",
  },
  {
    messageId: "def456",
    messageSender: "Textio",
  },
  {
    tomsBrilliantIdea: "Messages now have unique tracking codes",
    trackingCode: "trk-555888",
    loggedAt: "2025-02-07T09:30:00Z",
  },
];

for (const log of messageLogs) {
  printMatchingProperties(log, "message");
  printMatchingProperties(log, "log");
}
```

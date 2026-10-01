# Synchronous vs. Asynchronous
Most code is [synchronous](https://developer.mozilla.org/en-US/docs/Glossary/Synchronous), meaning it _runs in sequence_. Each line of code executes in order, one after the next.
[Synchronous Code](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/synchronous%20code.png)
Example of synchronous code:
```js
console.log("I print first");
console.log("I print second");
console.log("I print third");
```
Asynchronous, or [`async`](https://developer.mozilla.org/en-US/docs/Glossary/Asynchronous) code runs _concurrently_. While the [main thread](https://developer.mozilla.org/en-US/docs/Glossary/Main_thread) continues running subsequent code, async tasks are handled _outside_ the main execution flow & run as system resources allow. A good example is with the built-in [setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout)function.

`setTimeout` accepts a function & a number of milliseconds as inputs. It sets aside the function to be run after the number of milliseconds has passed, at which point it gets queued for execution when the main thread is available:
```js
console.log("I print first");
setTimeout(
  () => console.log("I print third because I'm waiting 100 milliseconds"),
  100,
);
console.log("I print second");

// Output:
// I print first
// I print second
// I print third because I'm waiting 100 milliseconds
```
### Assignment
Add times to the functions
```js
const textioSetupCompleteWait = 2000;
const errorHandlingWait = 1500;
const messageRoutingWait = 1000;
const smsProvidersWait = 500;

setTimeout(
  () => console.log("Textio setup complete!"),
  textioSetupCompleteWait,
);
setTimeout(
  () => console.log("Setting up error handling and retries..."),
  errorHandlingWait,
);
setTimeout(
  () => console.log("Configuring message routing..."),
  messageRoutingWait,
);
setTimeout(
  () => console.log("Connecting to SMS providers..."),
  smsProvidersWait,
);

console.log("Starting Textio service initialization...");

await sleep(2500);
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
```
# Why Async?

We try to _mostly_ write synchronous code when we can, because it's easier to keep track of, and therefore leads to fewer bugs. But sometimes we _need_ our code to be asynchronous. For example, whenever you update your user settings on a website, your browser needs to communicate those new settings to the server. The time it takes your HTTP request to physically travel across all the wiring of the internet can be anywhere from 10-1000 milliseconds (give or take).

It would be excruciating if your webpage froze while waiting for every network request to finish. By making network requests _asynchronously_, the webpage can continue to execute other code while waiting for the HTTP response to come back.

# Promises
[!Promises Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Promises-1920x1080.mp4)

A Promise in JavaScript is very similar to a promise to your friend. It's just a commitment for the future. For example, _I promise to explain promises to you._ This promise to you has 2 potential outcomes:

  * It's fulfilled, meaning I eventually explained
  * It's rejected, meaning I failed to explain

The [`Promise Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) represents the eventual **fulfillment or rejection** of a promise. In the meantime, while we're waiting for the promise to be fulfilled, our code continues executing. Promises are the most popular modern way to write asynchronous code in JavaScript.

## Creating a Promise

Here's a promise that, based on [random number generation](https://csrc.nist.gov/glossary/term/random_number_generator) will resolve & return the string "resolved!" or reject & return the string "rejected!" after 1 second:
```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    if (getRandomBool()) {
      resolve("resolved!");
    } else {
      reject("rejected!");
    }
  }, 1000);
});

function getRandomBool() {
  return Math.random() < 0.5;
}
```
In the `new Promise((resolve, reject) => { ... })` constructor, `resolve` & `reject` are functions provided by JavaScript that you call to either successfully complete the promise (`resolve`) or signal that it failed (`reject`)

## Working with Promises
Now that we've created a promise, how do we use it?

The `promise` object has `.then` & `.catch` methods. Think of `.then` as the _expected_ follow-up to a promise, & `.catch` as the "something went wrong" follow-up.
  * If a promise _resolves_, its `.then` method will execute.
  * If the promise rejects, its `.catch` method will execute.
```js
promise
  .then((message) => {
    console.log(`The promise finally ${message}`);
  })
  .catch((message) => {
    console.log(`The promise finally ${message}`);
  });

// if the promise (from the first example) resolves, the output will be:
// The promise finally resolved!

// if the promise rejects, the output will be:
// The promise finally rejected!
```
### Assignment
```js
function updateMessageStatus(messageId, currentStatus, isDelivered) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (currentStatus === "Sending") {
        if (isDelivered) {
          resolve(
            `Textio Message ${messageId} has been delivered successfully.`,
          );
        } else {
          reject(
            `Textio Message ${messageId} is still sending and cannot be marked as delivered.`,
          );
        }
      } else {
        resolve(
          `Textio Message ${messageId} status updated to ${currentStatus}.`,
        );
      }
    }, 500);
  });
}

export { updateMessageStatus };
```
# Why Promises?
Promises are the cleanest (but not the only) way to handle the common scenario where we need to make requests to a server, which is typically done via an [HTTP request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods). JavaScript's built-in [fetch()](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) returns a promise.

## I/O, or "input/output"
Almost every time you use a promise it will be to handle some form of I/O. I/O, or input/output, refers to when our code needs to interact with systems outside of the (relatively) simple world of local variables & functions.

Common examples of I/O include:
  * HTTP requests
  * Reading files from the hard drive
  * Interacting with a Bluetooth device
  * Sending data to a database

Promises help us perform I/O without forcing our entire program to freeze up while we wait for a response.
# Await
The [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) keyword is used to _wait_ for a Promise to resolve. Once it has been resolved, the `await` expression returns the value of the resolved `promise`. It's basically a more modern syntax for `.then` callbacks.

## .then Callback
```js
promise.then((message) => {
  console.log(`Resolved with ${message}`);
});
```
## await syntax
```js
const message = await promise;
console.log(`Resolved with ${message}`);
```

## Handling Rejections
When using `await`, if the promise is rejected, it will _throw an error_. That means we can use standard `try` / `catch` blocks to handle rejections.
```js
try {
  const message = await promise;
  console.log(`Resolved with ${message}`);
} catch (error) {
  console.log(`Resolved with ${error}`);
}
```
### Assignment
Complete the `updateMessageStatus` function
```js
const promise = updateMessageStatus("M123", "Sending", true);
const message = await promise;

console.log(message);

function updateMessageStatus(messageId, currentStatus, isDelivered) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (currentStatus === "Sending") {
        if (isDelivered) {
          resolve(
            `Textio Message ${messageId} has been delivered successfully.`,
          );
        } else {
          reject(
            `Textio Message ${messageId} is still sending and cannot be marked as delivered.`,
          );
        }
      } else {
        resolve(
          `Textio Message ${messageId} status updated to ${currentStatus}.`,
        );
      }
    }, 1000);
  });
}
```
# Async Keyword
Whille the `await` keyword can be used in place of `.then()` to _resolve_ a problem, the [async keyword](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) can be used in place of [new Promise()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/Promise) to _create_ a new promise. 

When a function is prefixed by the `async` keyword, it will _automatically_ return a Promise that resolves to the return value. You can think of `async` as "wrapping" your function within a promise.

These are equivalent:
## New Promise()
```js
function getPromiseForUserData() {
  return new Promise((resolve) => {
    fetchDataFromServer().then(function (user) {
      resolve(user);
    });
  });
}

const promise = getPromiseForUserData();
```
## Async
```js
async function getPromiseForUserData() {
  const user = await fetchDataFromServer();
  return user;
}

const promise = getPromiseForUserData();
```
> `await` can only be used inside an `async` function or at the top level of a module (file). In an `async` function, returning a `Promise`, will implicitly be awaited by the caller.

### Assignment
Update the `getMessageHash` function
```js
async function getMessageHash(sender, content) {
  const hash = await sha256Hex(content);
  return `Sender (${sender}): ${hash}`;
}

// don't touch below this line

async function sha256Hex(str) {
  const encoder = new TextEncoder();
  const data = encoder.encode(str);
  const hashBuffer = await crypto.subtle.digest("SHA-256", data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hex = hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  return hex;
}

export { getMessageHash };
```
# then vs. await
In the early days of web browsers, promises and the `await` keyword didn't exist, so the only way to do something asynchronously was to use callbacks. A "callback function" is a function you hand to another function. That function then calls your callback later on. The [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) function we've used in the past is a good example.
```js
function callbackFunction() {
  console.log("calling back now!")
}
const milliseconds = 1000;
setTimeout(callbackFunction, milliseconds);
```
The `.then()` syntax is generally _easier to then the non-`Promise` callbacks_, but `async` & `await` make handling promises even _simpler_. As a general rule, prefer `async` & `await` over `.then` and new Promise(). Realistically, what's going to be easier to follow & understand?
```js
fetchRecipient()
  .then(function (recipient) {
    return fetchMessageForRecipient(recipient.id);
  })
  .then(function (message) {
    return fetchDeliveryStatus(message.id);
  })
  .then(function (status) {
    console.log(`The status is ${status}`);
  });
```
```js
const recipient = await fetchRecipient();
const message = await fetchMessageForRecipient(recipient.id);
const status = await fetchDeliveryStatus(message.id);
console.log(`The status is ${status}`);
```

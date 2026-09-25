# Synchronous vs. Asynchronous
Most code is [synchronous](https://developer.mozilla.org/en-US/docs/Glossary/Synchronous), meaning it _runs in sequence_. Each line of code executes in order, one after the next.
[!Synchronous Code](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/synchronous%20code.png)
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

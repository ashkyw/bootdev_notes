# Single Threaded
JavaScript is _famously_ [single threaded](https://en.wikipedia.org/wiki/Thread_(computing)#Single-threaded_vs_multithreaded_programs).

![Threads video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/js-is-single-threaded-and-non-blocking-v3-1920x1080.mp4)

JavaScript, however, is incredible when it comes to asynchronous programming because it's "non-blocking".

The simplest way to think about it is that JavaScript can only execute one instruction at a time, but it can continue processing other stuff **while it's waiting** for something external (like a network request) to complete. In other words, if the "many things" you're doing are I/O bound, like:

  * Network Requests
  * File System Operations
  * Timers
  * Database queries

Then JavaScript performs quite well. If they're CPU bound (like heavy calculations), JavaScript will struggle. A Node.js server will often far outperform a multi-threaded Python, Ruby or PHP server because of its ability to handle many concurrent connections without much overhead. On the other hand, it will usually be outperformed by a multi-threaded Java, Go, C++, or Rust server when it comes to a heavy computation.
# Non Blocking
So how does JavaScript manage to be so efficient with asynchronous code? The answer is the [event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop).

The event loop is a single-threaded, non-blocking, event-driven, asynchronous execution model.

We've covered the single-threaded part, now let's examine [non-blocking](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model#never_blocking). Take this Python code for example:
```py
import time

print("Start")
time.sleep(2)
print("Middle")
time.sleep(2)
print("End")
```
This code prints "Start", then waits for 2 seconds, prints "Middle", waits another 2 seconds, & finally it prints "End". The `time.sleep(2)` function calls are _blocking_: they stop the program's execution until 2 seconds have passed.

Similarly in JavaScript:
```js
console.log("Start");
setTimeout(() => {
 console.log("End");
}, 4000);
console.log("Middle")
```
_This_ code prints "Start", then "Middle" _immediately_, waits 4 seconds, then prints "End". The main thread in JavaScript _cannot be blocked_. That's why `setTimeout` takes a callback function as an argument, it basically says:
> Hey, I know I can't block the program, but please Mr. JavaScript engine, can you take this function & run it for me in 4 seconds?

So, the main thread should _always_ be available to do work, and blocking (read: waiting) is delegated "for later".
### Assignment
Complete the `sleep(ms)` function
```js
function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
export { sleep };
```
# The Call Stack
![Call Stack](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Js_Event_Loop_V3-1920x1080.mp4)

So, we know that JavaScript has one main thread, & that it's non-blocking. So how do these "background" tasks (like HTTP requests, setTimeout, etc.) get executed? Well, it's via the [event loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop) - but first we need a little refresher on the call stack.

**Quick refresher:**
_Every time a function is called, it gets added to the top of the call stack. When a function returns, it gets popped off the stack_

Let's say we have this code:
```js
function startJob() {
 console.log("Job Started");
 workOnJob();
}

function workOnJob() {
 console.log("Working on job");
 finishJob();
}

function finishJob() {
 console.log("Job finished");
}

startJob();
```
The call stack will grow like this as each function is called:
```
                                      -> finishJob
                        -> workOnJob     workOnJob
[empty]    -> startJob     startJob      startJob
```
Then as each function returns it gets popped off the stack:
```
finishJob ->
workOnJob      workOnJob -> 
startJob       startJob       startJob ->  [empty]
```

Long story short - JavaScript's call stack works the same way as any other language's call stack. But what happens when we encounter asynchronous code? _That's in the next lesson_.
# Task Queue
We understand the call stack: call a function, it's pushed onto the stack, when it returns, it's popped off. But what about asynchronous code?

_Enter the task queue_.

The task queue (also known as the "message queue") is where asynchronous tasks are _queued up_ to be processed. It's just a standard queue of things for our JS engine to do, nothing to be scared of. But remember: Js is _non-blocking_, so the tasks in the queue can't be handled immediately.

The rule of the task queue is simple: when the call stack is _empty_, the event loop (managed by the JS runtime) checks the task queue. If there are tasks in the queue, it pushes the first one onto the call stack to be executed. Take a look at this example again:
```js
function startJob() {
  setTimeout(() => {
    console.log("Hi I'm async!");
  }, 0);
  console.log("Job started");
  workOnJob();
}

function workOnJob() {
  console.log("Working on job");
  finishJob();
}

function finishJob() {
  console.log("Job finished");
}

startJob();
```
Because the `setTimeout` says "run this 0 milliseconds from now", you _might_ expect its callback to run instantly & produce this output:
```
Hi I'm async!
Job started
Working on job
Job finished
```
But this is what actually happens:
```
Job started
Working on job
Job finished
Hi I'm async!
```
Because the callback:
```js
() => {
  console.log("Hi I'm async!");
};
```
Was pushed into the task queue to be executed _after_ the call stack is empty, & it's not empty until the final nested function `finishJob` returns.
### Assignment
Fix the scoping issue
```js
function processMessages(messages) {
  let success = true;
  console.log(`Processing messages: ${messages}`);
  setTimeout(() => {
    finalizeJob(success, messages);
  }, 0);
  if (messages < 0) {
    console.log("invalid data: how do we have negative messages??");
    success = false;
    return;
  }
  if (messages > 100) {
    console.log("invalid data: way too many messages");
    success = false;
    return;
  }

  console.log("Doing more stuff...");
}

function finalizeJob(success, messages) {
  const msg = success
    ? `Processed ${messages} successfully!`
    : `Failed to process messages!`;
  console.log(msg);
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

processMessages(42);
await sleep(0);
console.log("---");
processMessages(-1);
await sleep(0);
console.log("---");
processMessages(9001);
```
# Microtask Queue
As always, but wait...! There's (one) more (queue): the [microtask queue](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide).

Just like the task queue, the microtask queue is a mechanism for scheduling tasks to be executed later. But it operates under different rules & is used for different purposes. The nature of microtasks is that they represent smaller, shorter-lived operations compared to tasks in the task queue. And, importantly, **promises use the microtask queue** to schedule their `.then()` & `.catchk)` callbacks.

There are two important differences between the task queue & the microtask queue:
 
 * **Order of Execution**: All microtasks are executed before the next task in the task queue.
 * **Addition of Microtasks**: Microtasks can add more microtasks to the queue, and those will still execute before the next "macro" task.

## Do I Need to Care?
Usually, no. But sometimes yes. For the most part feel free to think about promises & callbacks as just "asynchronous operations that will run later". You typically won't (and it's often a bad sign if you do) care about the exact order that their callbacks will run.

This example shows the difference between the task queue & the microtask queue:
```js
function main() {
  console.log("main start");

  setTimeout(() => {
    console.log("macrotask 1 finished");
  }, 0);

  Promise.resolve()
    .then(() => {
      console.log("microtask 1 finished");
    })
    .then(() => {
      console.log("microtask 2 finished");
    });

  console.log("main end");
}

main();
// Prints:
// main start
// main end
// microtask 1 finished
// microtask 2 finished
// macrotask 1 finished
```
The important thing to note is simply that all the microtasks run before the next task in the task queue.
### Assignment
Fix the `processAnalytics` function
```js
async function processAnalytics(data) {
  let analysis = "";

  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(analysis);
    }, 100);

    setTimeout(() => {
      analysis += " - Finished!";
    }, 0);

    Promise.resolve().then(() => {
      analysis += `- Processing: ${data}`;
    });

    analysis += "Analyzing...";
  });
}

export { processAnalytics };
```
# Concurrency
Okay, so we understand that:
 * There's only one thread in the runtime
 * The main thread can't be blocked by asynchronous tasks
 * The results of asynchronous tasks are pushed into the task queue

So how does the actual concurrency work? In the case of:
```js
setTimeout(() => {
 consolle.log("Hi I'm async!");
}, 1000);
```
What logic makes sure that the calllback function isn't pushed into the task queue until `1000` milliseconds have passed? Or regarding an HTTP request, what logic pushed the network response into the task queue when the request is complete?

The answer is _external APIs_. Things like `setTimeout`, `fetch` & `addEventListener` are all examples of external APIs that the browser or Node.js, Deno, or Bun provide - they are not part of the core JavaScript language.

The JavaScript _runtime_ (your code & the JS engine) is single-threaded, but those external APIs are _not!_ The host environment can run them in the background (often on separate threads or system-level services), and **when they're done, the host environment pushes their results into the task queue** for the event loop to handle.

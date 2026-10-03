# Single Threaded
JavaScript is _famously_ [single threaded](https://en.wikipedia.org/wiki/Thread_(computing)#Single-threaded_vs_multithreaded_programs).

[!Threads video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/js-is-single-threaded-and-non-blocking-v3-1920x1080.mp4)

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

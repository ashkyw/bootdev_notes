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

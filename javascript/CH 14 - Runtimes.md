# JavaScript Runtimes

[JavaScript Runtimes Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/js-runtimes-1920x1080.mp4)

A runtime environment is _where your program runs_. The runtime you choose will determine things like:
  * What APIs are available to your code (fetch, canvas, etc.)
  * How your code is executed (JIT compiled vs interpreted)
  * What dependencies you'll need in production
  * Whether you run on the backend (a serve) or the frontend (a browser or mobile app)

## Examples of Runtimes
  * The browser (we try to pretend they're the same, but in reality different browsers are different runtimes)
  * [Node.js](https://nodejs.org/en/)
  * [A web worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers) (within a browser)
  * [Deno.js](https://deno.land/)
  * [Bun](https://bun.sh/)

Originally, JavaScript _only_ ran in browsers. Today, it runs almost everywhere.

## Which Runtime Should I use?
If you're doing frontend development, congratulations! You're using the browser. You likely have to support all the major browsers, so you'll need to know what APIs are available for each.

If you're doing backend development, you get to choose. Node.js is the oldest & most popular. Deno & Bun are newer & less mature, but have some cool features (like native Typescript support) & claim to be faster. In reality, they're all very similar to work with. You don't need to "learn" a runtime to be able to work with it. If you understand JavaScript, you can work with any of them.

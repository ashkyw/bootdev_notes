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

# Node.js
If you've used Python before, you're familiar with running a Python script like this:
```py
python main.py
```
Similarly, if you install [Node.js](https://nodejs.org/en/download/) toolchain on your local machine, you'll be able to run
```js
node main.js
```
Before Node, the only way to run JavaScript code was in the browser. Of course, you can still do that using [your browser's dev tools!](https://developer.chrome.com/docs/devtools/console/javascript/)

## NVM

Node Version Manager (NVM) makes it easy to:
 * Install multiple versions of Node
 * Update your Node version
 * Keep your Node version configurations separate on a per-project basis

It's kinda like `pyenv` for Python.

# NPM
Now that `node` is working, it's important to understand that... you probably won't use it directly very often. Instead, you'll use `npm` (Node Package Manager) to install & manage packages.

[`npm`](https://www.npmjs.com/) is a package manager for JavaScript. It's the world's largest software registry, with over 1.3 million packages of code. It's the home of many useful libraries such as:
 * [is-even](https://www.npmjs.com/package/is-even)
 * [cowsay](https://github.com/piuccio/cowsay)
 * [left-pad](https://www.npmjs.com/package/left-pad)

If you're familiar with Python, `npm` is similar to `pip` or `uv`. If you're familiar with Go, `npm` is similar to `go get`.

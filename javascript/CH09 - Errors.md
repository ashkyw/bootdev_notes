# Error Object
Errors in JavaScript, like Go, are called [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)s. It sure beats a silly name like "Exceptions"...

The most important property on the built-in [error object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) is the `message` property: which should be a human-readable description of the error:
```js
const err = new Error("We've run out of baked salmon");
console.log(err.message);
// We've run out of baked salmon
```

### Assignment
Complete `createError`
```js
function createError(message) {
  const errMsg = "Error: " + message;
  return new Error(errMsg);
}

export { createError };
```

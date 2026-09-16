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
# Handling Errors
Errors are thrown (and _should_ be thrown by _you_) when a non-happy path is encountered in your code. For example:
  * Data received from an API is not in the expected format
  * The connection to a database is lost
  * A user tries to log in with an incorrect password

Like Python, when an error is thrown, JavaScript yeets the program out of its current context & into the nearest [`try/catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) block, or, if there isn't one, it crashes the program. For example:
```js
const titan = {};
console.log(titan.neck.thickness);
console.log("done");
```
The above code prints:
```js
TypeError: Cannot read properties of undefined (reading 'thickness')
```
It never gets to the `console.log("done")` because the error crashes the program. But what if we use a `try/catch` block? We place the potentially error-throwing code in the `try` block, & if an error is thrown, execution immediately jumps the the `catch` block (ignoring any code in the `try` block that hasn't run yet):
```js
try {
  const titan = {};
  console.log(titan.neck.thickness);
  console.log("what's a titan?");
} catch (err) {
  console.log(err.message);
}
console.log("done");
```
Which prints:
```js
Cannot read properties of undefined (reading 'thickness')
done
```
### Assignment
Fix the error handling
```js
function main() {
  try {
    logObject(getMessageRecord(1));
    logObject(getMessageRecord(2));
    logObject(getMessageRecord(3));
    logObject(getMessageRecord(4));
  } catch (err) {
    console.log(err.message);
  }
}

// don't touch below this line

function getMessageRecord(messageId) {
  if (messageId === 1) {
    return { content: "Welcome to Textio!", timestamp: "2025-01-01T12:00:00Z" };
  }
  if (messageId === 2) {
    return {
      content: "Your order has shipped",
      timestamp: "2025-01-02T12:00:00Z",
    };
  }
  if (messageId === 3) {
    return {
      content: "Reminder: Payment due soon",
      timestamp: "2025-01-03T12:00:00Z",
    };
  }
  throw new Error("text id not found");
}

function logObject(obj) {
  for (const key in obj) {
    console.log(` - ${key}: ${obj[key]}`);
  }
  console.log("---");
}

main();
```
# Finally
We missed a block. While a `try/block` is the most common block you'll see, there is also a [`finally`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch#syntax) block. 
> The code in the `finally` block will always be executed _before_ control flow exits the entire construct.
It's for if you want something to run _regardless_ of what nonsense happens in the `try` & `catch` blocks. In some crazy scenarios (try to avoid this), you might have an error thrown in the `catch` block. But even if that happens, the `finally` block will still run. In this example:
```js
try {
  const titan = {};
  console.log(titan.neck.thickness);
  console.log("what's a titan?");
} catch (err) {
  console.log(err.message);
} finally {
  console.log("This will always run regardless of any errors.");
}
```
This is what gets printed:
```js
Cannot read properties of undefined (reading 'thickness')
This will always urn regardless of any errors.
```
### Assignment
Fix `Cleanup complete`
```js
function cleanup() {
  try {
    throw new Error("Textio processing failed");
  } catch (err) {
    throw new Error("Error in catch block");
  } finally {
    console.log("Cleanup complete");
  }
}

// don't touch below this line

try {
  cleanup();
} catch (err) {
  console.log(err.message);
}
```

# Objects
JavaScript [objects]() are an almost weirdly versatile collection type. Object literals (POJOs, or "plain old JavaScript objects") are often used to store data in key-value pairs
```js
const apple = {
  name: "Apple",
  radius: 2,
  color: "red",
}
```
You can access properties stored in an object using the `.` operator:
```js
console.log(apple.name); // prints "Apple"
console.log(apple.radius); // prints "2"
console.log(apple.color); // prints "red"
```
JavaScript objects are interesting because you'll use them the way you'd probably use a map or dictionary in other languages (simple key-value pairs),
but they can also be used for more complex things like classes & prototypes.

### Assignment
Complete the `createMessage` function:
```js
function createMessage(phoneNumber, message) {
  const messageToSend = {
    phoneNumber: phoneNumber,
    message: message,
    messageLength: message.length,
  };
  return messageToSend;
}

export { createMessage };

```

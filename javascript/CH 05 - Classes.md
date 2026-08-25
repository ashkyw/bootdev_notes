# Classes

[Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) in JavaScript are a _template_ for creating objects. As we learned, unlike many other languages, it's easy to create JavaScript objects _without_ classes, but that doesn't mean classes aren't useful.
```js
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const user = new User("Lane", 100);
```

* The [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class) declaration creates a new class
* The  [`constructor`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/constructor) method is a special method that's called when a new instance of the class (object) is created
* The [`new`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new) keyword calls the constructor method & creates a new instance of the class

### Assignment
Complete the `message` class.

```js
class Message {
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
  }
}

export { Message };
```
# Private Properties
By default, all properties of a class are public, meaning they can be accessed & modified from outside the class. Here's an example:
```js
class Movie {
  constructor(title, rating) {
    this.title = title;
    this.rating = rating;
  }
}
const matrixMovie = new Movie ("The Matrix", 9.5);
console.log(matrixMovie.title);
// The Matrix
matrixMovie.title = "The Matrix Reloaded";
console.log(matrixMovie.title);
// The Matrix Reloaded
```
Maybe we don't want our `title` to be able to be changed _anywhere in our code_. We can make it [private](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_properties) by prefixing it with a `#` & declaring it at the top of the class:
```js
class Movie {
  #title;
  constructor(title, rating) {
    this.#title = title;
    this.rating = rating;
  }
}
const matrixMovie = new Movie("The Matrix", 9.5);
console.log(matrixMovie.#title);
// Uncaught SyntaxError: Private field '#title' must be declared in an enclosing class
```
Private properties can still be used from within the class:
```js
class Movie {
  #title;
  constructor(title, rating) {
    this.#title = title;
    this.rating = rating;
  }

  getTitleAllCaps() {
    const allCaps = this.#title.toUpperCase();
    return allCaps;
  }
}

const matrixMovie = new Movie("The Matrix", 9.5);
console.log(matrixMovie.getTitleAllCaps());
// THE MATRIX
```
Encapsulation in JavaScript is typically enforced at two levels:
* **The class level**: Public/Private methods using `#` for private fields
* **The module level**: Exporting only what you want to be public
### Assignment
Make `createdAt` private
```js
class Message {
  #createdAt;
  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;
    this.#createdAt = new Date();
  }
}

const message = new Message("555-1234", "555-5678", "Hi there!");

console.log("Attempting to access the property createdAt...");
console.log("createdAt: " + message.createdAt);

const messageClass = Message.toString();
console.log("has private createdAt: " + messageClass.includes("#createdAt"));
```
# Static Methods
A [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static) method or property is bound to the class itself, not the instance of the class (an object). In this example, we create two instances of the `User` class:
```js
class User {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const lane = new User("Lane", 30);
const allan = new User("Allan", 30);
console.log(lane.name); // Lane
console.log(allan.name); // Allan
```
In JavaScript, a class is just an object template, so when we create a static method or property the object instances can't access it. So, the `static` members are often used for utility functions for the class itself.
```js
class User {
  static numUsers = 0;
  constructor(name, age) {
    this.name = name;
    this.age = age;
    User.numUsers++;
  }
  static getNumUsers() {
  return User.numUsers;
  }
}
  
  const lane = new User("Lane", 30);
  console.log(User.getNumUsers()); // 1
  const allan = new User("Allan", 30);
  console.log(User.getNumUsers()); // 2

  // This doesn't work because its not a method on the object
  console.log(lane.getNumUsers());
  // TypeError: lane.getNumUsers is not a function
  // at main.js:20:18
```
### Assignment
Add static properties to the `Message` class, Update the `Message` constructor, write a new static `getAverageMessageLength` method.
```js
class Message {
  static totalMessages = 0;
  static totalMessageLength = 0;

  constructor(recipient, sender, body) {
    this.recipient = recipient;
    this.sender = sender;
    this.body = body;

    Message.totalMessages++;
    Message.totalMessageLength += body.length;
  }

  static getAverageMessageLength() {
    const avg = Message.totalMessageLength / Message.totalMessages;
    return Math.round(avg * 100) / 100;
  }
}

export { Message };

```

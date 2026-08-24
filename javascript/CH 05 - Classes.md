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

# Prototypal Inheritance

[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Prototypes_And_Classes_In_Js_V2_-_Beast_Titan_Fix-1920x1080.mp4)

Classes are fairly new to JavaScript. They are not the underlying mechanism for inheritance, that's actually [prototypes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects/Object_prototypes). Classes are just syntactic sugar for prototypes.

Every object in JavaScript has a prototype. When an object "inherits" from another object, it's really that its parent is marked as its "prototype". It's called [prototypal inheritance](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain). The built-in [Object.create()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create) method creates a new object with its prototype set to the given object.
```js
const pureTitan = {
  // (define a parent object / prototype)
  name: "Eren's mom",
  speak(msg) {
    console.log("*titan noises*");
  },
};
pureTitan.speak();
// *titan noises*

const beastTitan = Object.create(pureTitan); // (define a child)

console.log(beastTitan.name); // (accessing .name from pureTitan)
// Eren's mom

beastTitan.name = "Zeke";
beastTitan.speak = function () {
  console.log(`${this.name} says, "I'm the Beast Titan"`);
};

beastTitan.speak();
// Zeke says, "I'm the Beast Titan"
```
### Assignment
Use `Object.create` to create a new `systemNotification` object that inherits its prototype from `notification`
Write a new method for `systemNotification` called `broadcast`.
```js
const notification = {
  notify(recipient, message) {
    return `Notification for ${recipient}: ${message}`;
  },
};

const systemNotification = Object.create(notification);
systemNotification.broadcast = function (message) {
  return `Broadcast to all users: ${message}`;
};

export { notification, systemNotification };
```
# Prototype Chains
Every object has a prototype, and that prototype can in turn have a prototype, creating a chain that goes all the way back to the [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object) object, whose prototype is always `null`.

**An object stores a reference to its prototype**. The [`Object.getPrototypeOf()`]() method returns the prototype of an object. When we create a new POJO (plain old java object), its prototype is automatically set to `Object.prototype`:
```js
const pureTitan = {
  name: "Eren's mom",
};

const beastTitan = Object.create(pureTitan);
beastTitan.name = "Zeke";

console.log(beastTitan); // { name: "Zeke" }
console.log(Object.getPrototypeOf(beastTitan)); // { name: "Eren's mom" }
console.log(Object.getPrototypeOf(beastTitan)) === pureTitan); // true
console.log(Object.getPrototypeOf(Object.getPrototypeOf(beastTitan))); // {} (Object.prototype)
console.log(
  Object.getPrototypeOf(
    Object.getPrototypeOf(Object.getPrototypeOf(beastTitan)),
  ),
); // null (end of the chain)
```

## How are Parent Members accessed?

You might think that using [`Object.create()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create) _copies_ the properties of parent object to the child object:
```js
const pureTitan = {
  name = "Eren's mom",
};

const beastTitan = Object.create(pureTitan);
console.log(beastTitan.name); // Eren's mom
```
**But it does not**. JavaScript looks within the `beastTitan` object for the `name` property & doesn't find it because we never set one. So it checks its prototype (using `Object.getPrototypeOf(beastTitan)`), which is `pureTitan`, and finds the `name` property there. It uses that value instead.

### Assignment
Write a the `isAdmin` function that takes an object & returns whether that object's prototype references the `adminUser` object.
```js
const user = {
  name: "Default User",
  type: "user",
};

const adminUser = Object.create(user);
adminUser.type = "admin";

function isAdmin(user) {
  return Object.getPrototypeOf(user) === adminUser;
}

export { user, adminUser, isAdmin };
```

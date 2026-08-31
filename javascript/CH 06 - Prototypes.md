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

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
# No Colon
The `key:value` syntax is the normal way to create key-value pairs in an object, but if you want a key to have the same name as an existing variable, you can omit the colon & the value. These are the same:
```js
const radius = 2;
const color = "red";
const apple = {
  radius: radius,
  color: color,
}
```
```js
const radius = 2;
const color = "red";
const apple = {
  radius, // same as radius: radius
  color: color, // set for demonstration
}
```
# Updating Properties
You can update and **add new** keys (you'll see the words "properties" and "key" used interchangeably here) to an existing object using the `.` operator. If it exists, it's updated; if it doesn't, it's created as a new property:
```js
const apple = {
  name: "Apple",
  radius: 2,
  color: "red",
};
apple.numSeeds = 3; // new property
apple.color = "green"; // update property
// {"name":"Apple", "radius":2, "color":"green", "numSeeds":3}
```
### Assignment
Complete the `addID` function
```js
function addID(campaignRecord) {
  campaignRecord.id = `${campaignRecord.campaignName}-${campaignRecord.senderName}`;
  return campaignRecord;
}

// don't touch below this line

export { addID };
```
# Nesting Properties
Objects can contain other objects. Here's two nested object literals within the `tournament` object:
```js
const tournament = {
  refree: {
    name: "Sally",
    age: 25,
  },
  prize: {
    units: "dollars",
    value: 100,
  },
};
```
We can access the nested properties the same way by chaining: `tournament.referee.name`
```js
console.log(tournament.referee.name); // Sally
console.log(tournament.referee.value); // 100
```
### Assignment
Finish the `getCampaignCreator` function
```js
function getCampaignCreator(campaign) {
  return campaign.creator.firstName;
}

export { getCampaignCreator };
```
# Optional Chaining
Nested data can _quickly_ become hard to work with. In most production systems you'll deal with 3-4 levels of object nesting on a regular basis. 
When using the normal `.` operator, if the object on the left side of the `.` is `null` or `undefined`, you'll get a `TypeError` at runtime. Thankfully, JavaScript has recently added a new operator to make dealing with this easier. The [optional chaining operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining): `?.`
```js
const tournament = {
  prize = {
    units: "dollars",
    value: 100,
  },
};

const h = tournament.referee.height;
// TypeError: Cannot read properties of undefined (reading: height)
```
So if you're _not sure_ whether the `referee` property exists we can use the optional chaining operator to avoid the error:
```js
const tournament = {
  prize = {
    units: "dollars",
    value: 100,
  },
};

const h = tournament.referee?.height;
// h is simply undefined, no error is thrown
```
### Assignment
Complete the `getRegion` function
```js
function getRegion(campaign) {
  return campaign.location?.region;
}

export { getRegion };
```
# When to Chain
You should only use `?.` chains when you _expect_ an object may not exist. For example, if according to our business logic, a `user` _must_ have an `address` object, but the `address` object may not have a `street` property, we wouldn't use the optional chaining operator because we expect `user.address` to never be `undefined`
```js
const street = user.address.street;
```
But if not all users have an address, we might use the optional chaining operator:
```js
const street = user.address?.street;
```
Or, is we aren't even sure if the `user` object exists:
```js
const street = user?.address?.street;
```
We don't want to overuse it because if we _expect_ that all users have objects, and we come across one that doesn't we probably _want_ an error thrown so we can see it and go fix the problem. _**Good Errors make debugging easier**_

# Object Methods
JavaScript objects can have `methods`, just like classes in Python or structs in Go. Objects are interesting in JavaScript because they play the role of dictionaries _&_ classes in other languages (Yes, JS also has classes, but more on that later). 

Methods are functions that are defined on an object. They can access & change the properties of the object in question. In the context of an object method, the `this` keyword refers to the object itself, like `self` in Python (more on the wonkiness of `this` later).
```js
const person = {
  firstName: "Lane",
  lastName: "Wagner",
  getFullName() {
    return this.firstName + " " + this.lastName;
  },
};

console.log(person.getFullName());
// Lane Wagner
```
### Assignment
Complete the `getRemainingMessages()` method in the `campaign` object.
```js
const campaign = {
  getRemainingMessages() {
    return this.maxMessages - this.sentMessages;
  },
  maxMessages: 100,
  sentMessages: 30,
  name: "Welcome Campaign",
};

// don't touch below this line

export { campaign };
```
# Methods Mutate
Methods can change the properties of their objects as well:
```js
const tree = {
  height: 256,
  color: "green",
  cut () {
    this.height /= 2;
  },
};

tree.cut();
console.log(tree.height);
// prints 128

tree.cut();
console.log(tree.height);
// prints 64
```
You might be wondering
> Wait... I thought `tree` was a constant?!?!

That is correct, but in JavaScript the `const` keyword doesn't stop you from _changing the **properties**_ of an object... it only stops you from reassigning the variable (`tree` in this case) to a _new_ object. **Do _NOT_ trust `const` objects to have constant contents!**
### Assignment
Complete the `sendMessage()` method on the `campaign` object.
```js
const campaign = {
  name: "Welcome Campaign",
  maxMessages: 100,
  sentMessages: 30,
  sendMessage() {
    this.sentMessages++;
  },
};

export { campaign };
```

# Initializing Props
If a property (key) doesn't exist when we try to access it with the `.` operator, we'll just get `undefined`. One way to check for this is by using the `!` (not) operator because `undefined` is "falsy" (meaning it evaluates to `false` in a boolean context). The syntax is simple:
```js
const balances = {
  lane: 100,
  breanna: 150,
  john: 200,
};

// if bob doesn't have a balance yet
// create a new prop for him
// set to 0
if (!balances.bob) {
  balances.bob = 0;
}
```
# Strings as Keys
Accessing a property like `desk.height` is great when the name of the prop is _static_, meaning you know the what it is _before_ runtime. But what if the key is dynamic? Like, what if the user enters a string & you need to use that as the lookup key?
_Bracket notation solves this._
```js
const desk = {
  wood: "maple",
  width: 100
};
console.log(desk.wood);
// prints "maple"

console.log(desk["wood"]);
// also prints "maple"

const key = "wood";
console.log(desk[key]);
// also prints "maple"
```
For example, maybe the key is passed in as a parameter to a function:
```js
function getLastName(lastNames, firstName) {
  return lastNames[firstName];
}
```
### Assignment
Complete the `getProviderCount` function
```js
function getProviderCount(provider, counts) {
  return counts[provider] ?? 0;
}

export { getProviderCount };
```
# This 
[Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/this-and-arrow-functions-js-1920x1080.mp4)

The [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this) keyword is perhaps one of the most rage-inducing parts of JavaScript. Once you understand it, it's not too bad, but it's not super intuitive.

Put simply, `this` refers to the context where a piece of code is executed. 
## Global Context:
`this` refers to the [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window) object in browsers or `module.exports` in Node.js (not `global`, as you might expect).
```js
// in a browser
console.log(this);
// Window {...}
```
```js
// in Node.js
console.log(this);
// {}
```
## Strict Mode
In [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) `this` is `undefined` in the global scope in both the browser & Node.js.
```js
"use strict"
console.log(typeof this);
// undefined
```
## Method Context
Inside a standard [method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Method_definitions) or a [constructor](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new), `this` refers to the object the method is called on.
```js
const myObject = {
  message: "Hello, World!",
  myMethod() {
    console.log(this);
    console.log(this.message);
  },
};
myObject.myMethod();
// { message: "Hello, World!", myMethod: [Function: myMethod] }
// Hello, World!
```
# Arrow Functions
[Fat arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions), or "arrow functions", are another way to define functions in JavaScript. Arrow functions are _newer_ than the `function` keyword, however unlike the `let/const` syntax, arrow functions are _sometimes_ better, not _always_ better.
```js
// declaring a function without a variable
function add(x, y) {
  return x + y;
}
```
```js
// declaring a function with a variable
const add = function (x, y) {
  return x + y;
};
```
```js
// using the fat arrow syntax
const add = (x, y) => {
  return x + y;
};
```
>Not the least bit confusing to do essentially the same thing in 3 different ways.

## What's the difference?
* Fat arrow functions are usually declared as variables, while the `function` keyword may or may not be declared as a variable.
* Fat arrow functions handle object scoping in a more intuitive way (more to come later)
* Fat arrow functions don't work as constructors (more, later)
* Other minor [differences](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#description)

### Assignment
Convert `isSpamMessage` to the fat arrow syntax
```js
const isSpamMessage = (message) => {
  if (message.toLowerCase().includes("offer")) {
    return true;
  }
  if (message.toLowerCase().includes("free")) {
    return true;
  }
  return false;
};

// don't touch below this line

function isFunctionType(f) {
  return f.hasOwnProperty("prototype");
}

function test(msg) {
  const isSpam = isSpamMessage(msg);
  console.log(`'${msg}' is spam: ${isSpam}`);
}

test("Get an offer now!");
test("Free beer in your local area");
test("Hey mom, sorry I couldn't make it to your birthday...");
console.log("========================");
if (isFunctionType(isSpamMessage)) {
  console.log("isSpamMessage is a classic function");
} else {
  console.log("isSpamMessage is a fat arrow function");
}

```
# Fat arrows & This
One reason to choose an arrow function over a regular `function` or method is to preserve the `this` context. It's particularly useful when working with objects. To be fair, in a simple object like this, the non-arrow method makes perfect sense:
```js
const author = {
  firstName: "Lane",
  lastName: "Wagner",
  getName() {
    return `${this.firstName} ${this.lastName}`;
  },
};
console.log(author.getName());
// prints Lane Wagner
```
With a fat-arrow function, the `this` keyword **refers to the same context as its parent**. In essence, **fat arrow functions "preserve" the `this` context**.
That's why this `this.firstName` and `this.lastName` are undefined in this example:
```js
const author = {
  firstName: "Lane",
  lastName: "Wagner",
  getName: () => {
    return `${this.firstName} ${this.lastName}`;
  },
};
console.log(author.getName());
// Prints: undefined undefined
// because `this` still refers to the global object
// and `firstName` & `lastName` are not defined globally
```
Devs working on front-end JavaScript frameworks (like React or Vue) _tend to use fat arrow functions often_. The `this` context can contain a _ton_ of component-wide state, and it needs to be preserved throughout nested function calls, so fat arrows make the code easier to read & write.
### Assignment
Revert the `sendMessage` method to a regular method
```js
const campaign = {
  name: "Welcome Campaign",
  maxMessages: 100,
  sentMessages: 30,
  sendMessage() {
    this.sentMessages++;
  },
};

// don't touch below this line

export { campaign };
```
# Spread Syntax
JavaScript has a really nifty [spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax#spread_in_object_literals) for moving groups of object properties around. It's a great way to copy objects & merge object properties.
```js
const engineering_dept = {
  lane: "grand magus",
  hunter: "software engineer",
  allan: "software engineer",
  matt: "software engineer",
  dan: "software engineer",
  waseem: "software engineer",
};

const video_dept = {
  stass: "video producer",
  alex: "video producer"
};

const all_employees = {... engineering_dept, ...video_dept};
/*
{
  lane: 'grand magus',
  hunter: 'software engineer',
  allan: 'software engineer',
  matt: 'software engineer',
  dan: 'software engineer',
  waseem: 'software engineer',
  stass: 'video producer',
  alex: 'video producer'
}
*/
```
The spread syntax [shallow copies](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy) the properties of the objects you're spreading. If properties have the same name, the last (right-most) object's property will overwrite the previous ones.
``` js
const engineering_dept = {
  lane: "software engineer",
  hunter: "software engineer",
};

const video_dept = {
  lane: "cringe youtuber",
  alex: "video producer",
};

const all_employees = {... engineering_dept, ...video_dept};
/*
{
  lane: 'cringe youtuber',
  hunter: 'software engineer',
  alex: 'video producer'
}
*/
```
### Assignment
Complete the `mergeTemplates` function. 
```js
function mergeTemplates(defaultTemplates, customTemplates) {
  return {...defaultTemplates, ...customTemplates};
}

export { mergeTemplates };
```
# Return Objects
In JavaScript you can only return a single value from a function. So, when we want to return multiple values, we just return an object that contains those values.
```js
function doAllTheMath(x, y) {
  const sum = x + y;
  const difference = x - y;
  const product = x * y;
  const quotient = x / y;
  return{
    sum,
    difference,
    product,
    quotient,
  };
}

const results = doAllTheMath(10, 5);
console.log(results.sum);
// 15
console.log(results.difference);
// 5
console.log(results.product);
// 50
console.log(results.quotient);
// 2
```
### Assignment 
Complete `calculateCampaignMetrics`
```js
function calculateCampaignMetrics(sent, opened, clicked) {
  const openRate = opened / sent;
  const clickRate = clicked / sent;
  const conversionRate = clicked / opened;
  return {
    openRate,
    clickRate,
    conversionRate,
  };
}

export { calculateCampaignMetrics };

```

# Object Literal Types
The most useful upgrade from JavaScript to TypeScript is adding types to objects.

[Object Literal Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) allows you to describe the shape of an object:
```ts
function logSaiyan(saiyan: { name: string; power: number }) {
  console.log(`${saiyan.name} has power lever: ${saiyan.power}!` );
}
```
Or, more likely, you'll define an object first:
```ts
type Saiyan = {
  name: string;
  power: number;
};

function logSaiyan(saiyan: Saiyan) {
  console.log(`${saiyan.name} has power lever: ${saiyan.power}!` );
}
```
This will make a red squiggly appear in your IDE if you misspell it in TypeScript. JavaScript won't fail until you run it
### Assignment
Fix & update `processMail`
```ts
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
};

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```
# Extra Properties
_Most of the time_, when you pass an object to a function in TypeScript, it's:
    * OK to have _more_ properties than those defined in the function's parameter type
    * Not OK to have _missing_ properties

However, when you pass an object _literal_ directly to a function, TypeScript performs what's called "excess property checking". Which means it _also_ will not allow extra properties.

For example, say we have this type:
```ts
type Spaceship = {
  name: string;
  speed: number;
};
```
and we make an object with one extra property:
```ts
const Falcon = {
  name: "Millennium Falcon",
  speed: 75,
  weapons: 4, 
};
```
We can pass this object to a function that expects a `Spaceship`:
```ts
function pilot(ship: Spaceship) {
  console.log(`Piloting ${ship.name} at ${ship.speed} light-years per hour` );
}
// this is fine
pilot(falcon);
```
But interestingly, if we pass in the same object _literal_ (no variable assignment), TypeScript will throw an error:
```ts
// Error: Object literal may only specify known properties, and 'weapons' does not exist in type 'Spaceship'.
pilot({ name: "Millennium Falcon", speed: 75, weapons: 4 });
```
_It's also worth noting that many of these kinds of rules are configurable in the [`tsconfig.json`](https://www.typescriptlang.org/tsconfig)_file_.
### Assignment
Fix the `Mail` type
```ts
export type Mail = {
  from: string;
  to: string[];
  cc: string[];
  subject: string;
  body: string;
  urgent: boolean;
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to.join(", ")}
CC: ${mail.cc.join(",")}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```
# Optional Object Properties
Optional properties can be added to an object type with the `?` operator.
```ts
type Superhero = {
  name: string;
  strength: number;
  cape?: boolean // cape is optional
};
```
That means that the type of `.cape` is actually `boolean | undefined`, just like optional function parameters
> [!TIP]
> Do _not_ go overboard using optional properties. Require all the fields that **should** be there. It will make your life easier with and you won't
> have so many runtime checks that look like this:

```ts
function fight(superhero: Superheor) {
  if (!superhero.cape) {
  // something
  }
// happy path thing
}
```
### Assignment
Fix the `Mail` type.
```ts
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
  cc?: string[];
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}${!mail.cc ? "" : "\nCC: " + mail.cc}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```
# Empty Object Type
Let's says we create a new empty object:
```ts
let newUser = {};
```
Then go to add properties to it later:
```ts
// Propertiy 'name' does not exist on type '{}'
newUser.name = "Lane";
```
**TypeScript doesn't like that!**

It make sense, we never told TypeScript which properties to allow, but here's what's really crazy: _this_ is actually allowed:
```ts
let newUser = {};
newUser = "Lane";
```
That is correct: you can reassign the variable which initially held an empty object to a _string_. In fact, you can reassign it to anything except `null` or `undefined`, because everything else is technically an object! So, to get back to our first example, what you probably _want_ to do is just predefine the allowed fields:
```ts
type User = {
  name: string;
};

let newUser: User = {
  name: "Lane",
};
```
### Assignment
Fix the `Address` type
```ts
export type Address = {
  name: string;
  domain: string;
};

// don't touch below this line

export type Mail = {
  from: Address;
  to: Address[];
  subject: string;
  body: string;
  urgent: boolean;
  cc?: Address[];
};

export function processMail(mail: Mail) {
  let addressees = "";
  for (const addressee of mail.to) {
    addressees += `${addressee.name}@${addressee.domain}, `;
  }
  addressees = addressees.slice(0, -2);

  let copies = "";
  if (mail.cc) {
    copies = "\nCC: ";
    for (const addressee of mail.cc) {
      copies += `${addressee.name}@${addressee.domain}, `;
    }
    copies = copies.slice(0, -2);
  }

  return `FROM: ${mail.from.name}@${mail.from.domain}
TO: ${addressees}${copies}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```
# Discriminated Unions
A union of two primitive types, like `string | number`, is really simple: it's a string or a number. The same is true of object types, but it can be tricky to know which type you're dealing with. That's where "discriminant properties" (or "tags") come in handy. It's just a property that tells you which type you're dealing with, & makes it easy to use conditional logic to handle each type. What is special about it is it can only be one value.

Unions of objects with a discriminant property are called ["discriminated unions"](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-func.html#discriminated-unions) or "tagged unions".
```ts
type MultipleChoiceLesson = {
  kind: "multiple-choice"; // Discriminant Property
  question: string;
  studentAnswer: string;
  correctAnswer: string;
};

type CodingLesson = {
  kind: "coding"; // Discriminant property
  studentCode: string;
  solutionCode: string;
};

type Lesson = MultipleChoiceLesson | CodingLesson;

function isCorrect(lesson: Lesson): boolean {
  switch (lesson.kind) {
    case "multiple-choice":
      return lesson.studentAnswer === lesson.correctAnswer;
    case "coding":
      return lesson.studentCode === lesson.solutionCode;
  }
}
```
Discriminated unions are **really** useful when you need to account for another new shape because TypeScript can ensure you handle all the possible cases. If we make these changes:
```ts
type TrueFalseLesson = {
  kind: "true-false"; // Discriminant property
  question: string;
  studentAnswer: boolean;
  correctAnswer: boolean;
};

type Lesson = MultipleChoiceLesson | CodingLesson | TrueFalseLesson;
```
TypeScript will throw an error: `Function lacks ending return statement and return type does not include 'undefined'`. Which reminds us to add a third case:
```ts
function isCorrect(lesson: Lesson): boolean {
  switch (lesson.kind) {
    case "multiple-choice":
      return lesson.studentAnswer === lesson.correctAnswer;
    case "coding":
      return lesson.studentCode === lesson.solutionCode;
    case "true-false":
      return lesson.studentAnswer === lesson.correctAnswer;
  }
}
```
> [!TIP]
> You don't _have_ to use `kind` as the tag. But the convention generally does. Follow the convention.

### Assignment
Create the `Address` type
```ts
type InternalAddress = {
  kind: "internal";
  firstName: string;
  lastName: string;
};

type ExternalAddress = {
  kind: "external";
  username: string;
  domain: string;
};

// don't touch below this line

export type Address = InternalAddress | ExternalAddress;

export function formatAddresses(addresses: Address[]) {
  let formatted = "";
  for (const address of addresses) {
    if (address.kind === "internal") {
      formatted += `${address.firstName}.${address.lastName}@support.ai, `;
    }
    if (address.kind === "external") {
      formatted += `${address.username}@${address.domain}, `;
    }
  }
  return formatted.slice(0, -2);
}
```
# Sets
TypeScript has a built-in type for [sets](), which are collections of unique values. You can ensure that all the values in the set are of the same type by specifying a type parameter `<T>`.
```ts
// A set that contains only strings
const justiceLeague = new Set<string>();

justiceLeague.add("Green Arrow");
justiceLeague.add("Flash");

// Error: Argument of type 'number' is not assignable to parameter of type 'string'
justiceLeague.add(2);
```
An array can be converted into a set, which automatically removes duplicate values:
```ts
// A Set automatically removes duplicate values from an array
const names = ["plasticman", "firestorm", "plasticman"];
const justiceLeague = new Set <string>(names);

console.log(justiceLeague);
// Set(2) { 'plasticman', 'firestorm' }
```
Sets also have a few other interesting methods & properties:
  * [delete()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete)
  * [has()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/has)
  * [forEach()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/forEach)
  * [size](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/size)
```ts
const justiceLeague = new Set<string>(["Atom", "Black Canary", "Blue Beetle"]);

console.log(justiceLeague.size); // 3
justiceLeague.delete("Blue Beetle");
console.log(justiceLeague.has("Blue Beetle")); // false

justiceLeague.forEach((member) => console.log(member));
// Atom
// Black Canary
```
### Assignment
Complete the `findNumUniqueLabels` function
```ts
export function findNumUniqueLabels(formattedAddresses: string[]) {
  const uniques = new Set(formattedAddresses);
  return uniques.size;
}
```

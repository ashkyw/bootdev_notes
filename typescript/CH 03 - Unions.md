# Unions
[Union types]() use the pipe symbol `|` & allow you to specify that a value can be one of several types.
```ts
// userId is a string OR a number
let userId: string | number;
userId = "user_42";
userid = 42;
```
Unions are perfect for when a value could be one of several types. One really cool thing about TypeScript is that conditional checks actually change the type of a variable.This is called "type narrowing":
```ts
function safeSquare(val: string | number): number {
  if (typeof val === "string") {
    val = parseInt (val,10);
  }
  // now val is only a number
  return val * val;
}

let result = safeSquare("5");
console.log(result);
// 25


let result = safeSquare(5);
console.log(result);
// 25
```
### Assignment
1. Update the `getTicketInfo` function to only accept an `id` that's a string or a number.
2. If `id` is a string, parse the number out of it
3. Return the string `Processing ticket: ID` where `ID` is the ID number or the parsed number from the project code.
```ts
export function getTicketInfo(id: string | number) {
  if (typeof id === "string") {
    const [_, idNum] = id.split("-");
    return `Processing ticket: ${idNum}`;
  }
  return `Processing ticket: ${id}`;
}
```
# Optional Parameters
You can specify function parameters as _optional_ with a question mark (`?`) after the name:
```ts
function greet(name: string, title?: string): string {
  if (title) {
    return `Hello, ${title} ${name)!`;
  }
  return `Hello, ${name)!`;
}

greet("Gandalf"); // Hello, Gandalf!
greet("Gandalf", "Wizard"); // Hello, Wizard Gandalf!
```
There are two rules to keep in mind:
  1. Optional parameters must come _**after**_ all required parameters.
  2. Optional parameters have an `undefined` automatically unioned on the specified type. If the value is omitted, it's `undefined` instead of the specified type.

### Assignment
1. Modify the `calculateApiCost` function to make `tier` optional
2. `calculateApiCost` should return the cost of api calls:
  * No tier, or tier not recognized = `0.10`
  * `pro` tier = `0.05`
  * `enterprise` tier = `0.03`
```ts
export function calculateApiCost(numReqs: number, tier?: string) {
  let cost = 0.10;
  if (tier === "pro") {
    cost = 0.05;
  } else if (tier === "enterprise") {
      cost = 0.03;
  }
    return numReqs * cost;
}
```
# Default Parameters
Default parameters provide fallback values for arguments that callers can omit.
```ts
function newCharacter(name: string, role: string = "warrior"): string {
  return `${name} is a ${role}`;
}

console.log(newCharacter("Gandalf"));
// Gandalf is a warrior
console.log(newCharacter("Gandalf", "wizard"));
// Gandalf is a wizard
```
When you use default parameters, you do _not_ need to mark the parameter as optional by using `?`. When using a default value, the parameter type can be automatically inferred, so don't specify it (unless you need to widen the type):
```ts
function countdown(start = 10): void {
  // start is a number
  console.log(`Counting down from ${start}...`);
}
```
### Assignment
1. Complete `estimateResponseTime`
2. Calculate the estimated response time based on `modelType`
     * `text`: `2+(0.01 * prompLength)` seconds
     * `image`: `5+(0.02 * prompLength)` seconds
     * `code`: `3+(0.05 * prompLength)` seconds
     * otherwise `0`
3. Return the final time in seconds, rounded to the nearest whole number
```ts
export function estimateResponseTime(promptLength = 100, modelType = "text") {
  let time = 0;
  if (modelType === "text") {
    time = 2 + (0.01 * promptLength);
  } else if (modelType === "image") {
    time = 5 + (0.02 * promptLength);
  } else if (modelType === "code") {
    time = 3 + (0.05 * promptLength);
  }
  return Math.round(time);
}
```
# Literal Types
Many other statically typed languages don't have nearly as extensive & powerful type systems as TypeScript. It should be obvious, since it's in the name, but TypeScript has a massive type system.

[Literal Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#literal-types) are incredibly powerful for narrowing the possible values of a variable.

  * A string can have an infinite number of values.
  * A number can have an infinite number of values

So what if we want to declare a "direction" variable?
```ts
function move(direction: string) {
  // Implementation...
}
```
This sucks, direction can be any string! To be fair, in many other languages enums are used to solve this problem. While TypeScript does have enums, literal types are a more lightweight solution. I literal value can be used as a type:
```ts
function move(direction: "north") {
  // Implementation...
}
```
Now `direction` can _only_ be "north".
# Value Unions
Let's look at the last example of a literal type:
```ts
function move(direction: "north") {
  // Implementation...
}
```
Now, let's make it a bit more useful & combine that idea with a union type:
```ts
function move(direction: "north" | "south" | "east" | "west") {
  // Implementation...
}
```
But, let's refactor it to make a new "Direction" type that we can reuse:
```ts
type Direction = "north" | "south" | "east" | "west";

function move(direction: Direction) {
  // Implementation...
}
```
### Assignment
1. Create and `export` a new `Priority` type.
2. Update the `setPriority` function to accept the `Priority` typed instead of any `string`
3. Complete the `setPriority` function.
```ts

```

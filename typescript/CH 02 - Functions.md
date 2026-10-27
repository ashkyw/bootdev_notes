# Function Type Syntax
One of the most useful places for explicit types is in function signatures.
```ts
function createMessage (name: string, a: number, b: number): string {
  return `${name} scored ${a+b}`;
}
```
The `:type` after each parameter specifies that parameter's type, and the `:type` after _all_ the parameters specifies the return type. It works the same way with arrow functions:
```ts
const createMessage = (name: string, a: number, b: number): string => {
  return `${name} scored ${a + b}`;
};
```
### Assignment
Fix the typing for `calculateTotal`
```ts
export function calculateTotal(
  price: number,
  quantity: number,
  discount: number,
): number {
  return price * quantity * (1 - discount);
}
```
# Inferred Return Types
We've discussed that:
```ts
const myPowerLevel = 9000;
```
Is better than:
```ts
const myPowerLevel: number = 9000;
```
Thus instead of:
```ts
function divide(a: number, b: number): number {
  return a / b;
}
```
We can write:
```ts
function divide(a: number, b: number) {
  return a / b;
}
```
And TypeScript infers the output type as `number`.

[Why are Inferred Return types better?](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/inferred-return-types-1920x1080.mp4)
### Assignment
Complete `combinePrompts` using inferred return it should:
  * Take two strings
  * Return them concatenated by `\n`
```ts
export function combinePrompts(systemPrompt: string, userPrompt: string) {
  return `${systemPrompt}\n${userPrompt}`;
}
```
# Void
The TS-specific [`void`]() type represents the return value of functions that _don't_ return a value.
```ts
function logMessage(message: string): void {
  console.log(message);
  // nothing is returned here!
}
```
In JavaScript, a function without a `return` statement returns `undefined` by default... but that's kinda vague. TypeScript uses the `void` keyword to indicate that truly _nothing_ is returned.

In other words, `void` more explicitly communicates the _intent_ that a function returns _nothing_.
### Assignment
Update the `logSystemEvent` function to return the log as a string instead of logging it to the console.
```ts
export function logSystemEvent(
  event: string,
  severity: "info" | "warning" | "error",
): string {
  return `SYSTEM ${severity.toUpperCase()}: ${event}`;
}
```
# Function Types
Functions themselves are values in JavaScript (and by extension TypeScript), which means they must also have a type.
In TypeScript, a function's type includes information about its parameters & return value.

## Defining Function Types
The syntax for a function type looks like this:
```ts
(param1: type, param2: type, ...) => returnType
```
For example, a function that takes two numbers & returns a number:
```ts
(a: number, b: number) => number;
```
and both of these functions are of that type:
```ts
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
```
# Type Alias
It can get really cumbersome to write out long custom types whenever you want to use them. For example, maybe we have a function that accepts another function as input.
```ts
function setLoggerTimeout(
  loggerCallback: (s1: string, s2: string) => string,
  delay: number,
) {
  // do something
}
```
That's a really nasty function signature. Let's use [`type keyword`](https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html#reusable-types-type-aliases) instead to create an aliasaa
```ts
type LoggerCallback = (s1: string, s2: string) => string;
```
Now whenever we use this specific kind of function we can just use `LoggerCallback`:
```ts
function setLoggerTimeout(loggerCallback: LoggerCallback, delay: number){
// something
}
```
> [!TIP]
>A function type alias describes a function's shape; it doesn't declare or create functions. You don't need to explicitly use the alias in your function declarations – as long as the signature matches, the function "conforms to" the type. 
This is much easier to read an reuse. 
### Assignment
1. Create and `export` a new `SupportResponse` function that takes a string & returns a string
2. Update `greetCustomer` so its signature conforms to `SupportResponse`
3. Repeat for `farewellCustomer`
```ts
export type SupportResponse = (name: string) => string;

export function greetCustomer(name: string) {
  return `Hello ${name}, welcome to Support.ai! How can I assist you today?`;
}

export function farewellCustomer(name: string) {
  return `Goodbye ${name}, have a great day!`;
}
```
#### Notes from the Boots AI
  1. **Parameter naming vs. types**:
     In `greetCustomer(SupportResponse: string)`, `SupportResponse` became the _name_ of the parameter variable (holding a string), not its type. It
     technically worked because the function still took one string and returned a string, but idiomatic code would keep the parameter name as `name: string`.
  2. **Structural Typing**:
     TypeScript checks whether types match by their _shape_, not their name. When you define:
     ```ts
       export type SupportResponse = (name: string) => string;
     ```
     and then write:
     ```ts
       export function greetCustomer(name: string) {
         return `Hello ${name}...`;
       }
     ```
TypeScript looks at `greetCustomer` and sees:
  * Takes a `string`
  * Returns a `string`

Because the shape matches `(name: string) => string`, TypeScript allows `greetCustomer` to be assigned to any variable or parameter typed as `SupportResponse`.
You don't have to explicitly mention `SupportResponse` inside `greetCustomer` at all for it to satisfy the type.
# Importing Types
With certain TypeScript configurations you _can_ import types directly from a module:
```ts
import { User, Post } from "./models";
```
But it's much safer & _more efficient_ to use the `import type` syntax:
```ts
import type { User, Post } from "./models";
```
This way TypeScript knows that you're only importing types, & it can drop the imports so they don't generate extra JavaScript code when your project is compiled. This means a smaller final bundle size. This syntax also works:
```ts
import { type User, type Post } from "./models";
```
But the first one is more concise.
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

```

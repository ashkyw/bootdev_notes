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
This is much easier to read an reuse. 
### Assignment
1. Create and `export` a new `SupportResponse` function that takes a string & returns a string
2. Update `greetCustomer` so its signature conforms to `SupportResponse`
3. Repeat for `farewellCustomer`
```ts

```

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

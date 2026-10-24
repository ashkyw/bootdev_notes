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

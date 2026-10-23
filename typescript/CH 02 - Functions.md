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

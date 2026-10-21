# TypeScript
[TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html) adds static typing to JavaScript, catching many kinds of bugs before your code even runs.

### Assignment
Fix the code:
> The `:string` annotation tells the TypeScript compiler that `bootupMessage` holds a string
```ts
const bootupMessage: string = "starting server...";
console.log(bootupMessage);
```
# Basic Types
TypeScript adds type annotations to JavaScript variables using a `:` followed by the type. The most common primitive types are:
```ts
const bootupMessage: string = "starting server...";
const port: number = 3000;
const isOnline: boolean = true;
const noValue: null = null;
const notDefined: undefined = undefined;
```
If a value doesn't match its type, the TypeScript compiler reports an error:
```ts
const bootupMessage: string = 123;
// Error: Type 'number' is not assignable to type 'string'
```

### Assignment
Fix `supportAiLogs` so it's a string
```ts
const supportAiLogs: string = "CRITICAL: Boots cut the power cord again";
console.log(supportAiLogs);
```

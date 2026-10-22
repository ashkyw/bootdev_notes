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
# Type Inference
[Type inference](https://www.typescriptlang.org/docs/handbook/type-inference.html) lets TypeScript determine a variable's type _from its value_, so we don't need to write obvious annotations.
```ts
// explicit (unnecessary)
const bootupLog: string = "starting server...";

// inferred (preferred)
const bootupLog = "starting server...";
```
Both versions are type-safe, but the inferred version is shorter.
### Assignment
Fix the type error:
```ts
const supportAiLogs = "WARNING: The break fridge smells like salmon";
console.log(supportAiLogs);
```
#  Why TypeScript
TypeScript is a [superset](https://www.cuemath.com/algebra/superset/) of JavaScript, meaning that:
  * All JavaScript code is valid TypeScript code.
  * All TypeScript code is not necessarily valid JavaScript code.

The _real_ question is why should I use TypeScript instead of JavaScript? TypeScript is fantastig because it:
  * Catches a ton of bugs & errors at compile time (fact)
  * Makes your code more readable & maintainable (opinion)
  * Makes it eaiser to refactor & scale your codebase (opinion)

In short, it adds static typing to JavaScript. 

# ![Story Time](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/what-is-typescript-1920x1080.mp4)
TypeScript was developed internally at Microsoft by C# devs who wanted static typing in their JavaScript. It was released publically in 2012. While its execution speed isn't necessarily blazing fast, its rise in popularity is.

# What is TypeScript
TypeScript is a _language_, but the official _implementation_ of TypeScript is the [TypeScript compiler](https://code.visualstudio.com/docs/typescript/typescript-compiling), `tsc`. Its job is simple: take TypeScript code, ensure it's valid, then compile it into JavaScriptcode.
> [!]
> The compiler (`tsc`) has been written in TypeScript for a long time, but _very_ recently, the TypeScript team has started a [port to Golang](https://github.com/microsoft/typescript-go)! They've reported compilation speed improvements of ~10x

TypeScript is _not_ supported natively by most JavaScript engines, so it needs to be compiled into equivalent JavaScript code before it can run. This interesting fact, that TypeScript is only type-checked _before_ it's run has led to an interesting question:

> Is TypeScript basically just a really good [linter](https://en.wikipedia.org/wiki/Lint_(software))?

Honestly? Yeah, essentially. Technically it does a _lot_ more than your standard linter, but from a practical perspective, its primary benefit is to do static analysis on your _almost-JavaScript_ code & catch bugs before they happen.

## Compiled to... JavaScript?
TypeScript is interesting in that it's "compiled", but not in the traditional (compiled to binary) sense. Instead, it's compiled to JavaScript. So it's not really compiled for _performance_ reasons, but rather _compatibility_ reasons.

**The goal of TypeScript is to write JavaScript code that's eaiser to work with**.

### Assignment
Fix the compilation error by changing the _value_ of `supportAiPort` to the _number_ `3000`
```ts
const supportAiPort: number = 3000;
console.log(`Starting server on port ${supportAiPort}...`);
console.log(`The type of supportAiPort is ${typeof supportAiPort}`);
```

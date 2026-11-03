# [Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
The most common way to declare an [array](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#arrays) is using the bracket notation, `string[]`, `number[]`, etc:
```ts
function trainJedi(jediKnights: string[]) {
  for (let knight of jediKnights) {
    console.log(`Training ${knight}...`);
  }
}

trainJedi(["Dooku", "Qui-Gon", "Xanatos"]);
// Training Dooku...
// Training Qui-Gon...
// Training Xanatos...
```
### Assignment
Complete the `averageScore` function. 
```ts
export function averageScore(ratings: number[]) {
  if (ratings.length === 0) {
    return 0;
  }
  let total = 0;
  for (const rating of ratings) {
    total += rating;
  }
  return total / ratings.length;
}
```
# Type Parameters
TypeScript offers an alternative way to declare arrays using type parameter syntax: `Array<T>`. It's basically the same thing as `T[]`

These function declarations are the same:
```ts
// Using bracket notation
function assignLightsaberColors(name: string, colors: string[]): void {
  // ...
}
// Using generic type parameter syntax
function assignLightsaberColors(name: string, colors: Array<string>): void {
  // ...
}
```
You can also use _either_ syntax when declaring variables:
```ts
const colors: string[] = [
  "blue",
  "green",
  "purple",
  "red",
  "orange",
  "white",
  "darksaber",
];
const midichlorianCounts: Array<number> = [
  1000, 5000, 12000, 20000, 27000, 40000,
];
```
When talking about [generics]() it will make more sense why one might choose to use `Array<T>` over `T[]` - mostly because it will feel _consistent_ with other generic types.
# Heterogeneous Arrays
If you can do it in JavaScript, you can model it in TypeScript. It might not always be _pretty_, but in this case it is!

In languages like Go, you can't have an array that contains different types - at least not without using something a bit more complex like a struct or an interface. But in TypeScript, we can just [union](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types) types!
```ts
// TypeScript infers the type as (string | number)[]
let lightsaberStyles = [1, 2, "double", "shoto"];

function describe(style: string | number): void {
  console.log(`Wield ${style} lightsaber`);
}

lightsaberStyles.forEach(describe);
// Wield 1 lightsaber
// Wield 2 lightsaber
// Wield double lightsaber
// Wield shoto lightsaber
```
Just use a `|`  to create union types. Easy!
### Assignment
Complete the `interpolateComment` function
```ts
export function interpolateComment(
  id: number,
  comment: string,
  comments: (string | number)[],
) {
  const index = comments.findIndex((c) => c === id);
  if (index !== -1) {
    comments[index] = comment;
  }
}
```

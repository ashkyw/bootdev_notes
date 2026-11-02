# Arrays
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

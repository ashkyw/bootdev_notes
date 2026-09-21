# Sets
JavaScript added support for sets. A set is just a collection of unique values. [Sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) are fantastic for de-duplication & checking if a value still exists in a collection.
```js
const set = new Set([1, 2, 3, 4, 5, 5, 5, 5]);
console.log(set);
// Set {1, 2, 3, 4, 5}
```
Notice that all duplicate instances of `5` were removed from the set. You can also [`add`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/add) & [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/delete) values dynamically:
```js
const set = new Set();
set.add("berholdt");
set.add("reiner");
set.add("annie");
set.add("berholdt");
// Set {'berholdt', 'reiner', 'annie'}

set.delete("annie");
console.log(set);
// Set {'berholdt', 'reiner'}
```

`...` spread operator also works on sets

### Assignment
Compelete the `deduplicateEmails` function
```js
function deduplicateEmails(emails) {
  const dedupedEmails = new Set(emails);
  return [...dedupedEmails];
}

export { deduplicateEmails };

```
# Set methods
## Intersection
The [`.intersectionn()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/intersection) method returns a new set containing the elements that are in _both_ sets
```js
const heroes = new Set(["eren", "miakas", "armin", "reiner"]);
const villains = new Set(["eren", "reiner", "bertholdt", "annie"]);
const samesies = heroes.intersection(villains);
console.log(samesies);
// Set {'eren', 'reiner'}
```
## Difference
The [`.difference()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/difference) method returns a new set containing the elements that are in the _first_ set but _not_ in the second set.
```js
const heroes = new Set(["eren", "mikasa", "armin", "reiner"]);
const villains = new Set(["eren", "reiner", "bertholdt", "annie"]);
const nonVillains = heroes.difference(villains);
console.log(nonVillains);
// Set { 'mikasa', 'armin' }
```
## Union
The [`.union()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set/union) method returns a new set containing the elements that are in _either_ set.
```js
const heroes = new Set(["eren", "mikasa", "armin", "reiner"]);
const villains = new Set(["eren", "reiner", "bertholdt", "annie"]);
const everyone = heroes.union(villains);
console.log(everyone);
// Set { 'eren', 'mikasa', 'armin', 'reiner', 'bertholdt', 'annie' }
```

There are more [set methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set#set_composition), but those are the big three.

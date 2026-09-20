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

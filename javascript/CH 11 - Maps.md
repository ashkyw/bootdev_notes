# Maps
JavaScript also offers support for _maps_: collections of key-value pairs. Map keys are unique, so adding a key that already exists will replace its value. You can [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/set) & [`delete`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map/delete) entries dynamically:
```js
const map = new Map();
map.set("bertholdt", "shifter");
map.set("reiner", "warrior");
map.set("annie", "shifter");
map.set("bertholdt", "colossal titan");
console.log(map);
// Map { 'bertholdt' => 'colossal titan', 'reiner' => 'warrior', 'annie' => 'shifter' }

map.delete("annie");
console.log(map);
// Map { 'bertholdt' => 'colossal titan', 'reiner' => 'warrior' }
```
Maps can be constructed from any iterable. Maps are iterable, so that means the `Map` constructor can accept a map:
```js
const originalMap = new Map();
originalMap.set("bertholdt","shifter");
const mapCopy = new Map(originalMap);
console.log(mapCopy);
// Map { 'bertholdt' => 'shifter' }
```
### Assignment
Complete the `addToPhoneBook` function
```js
function addToPhonebook(phoneNumber, name, phoneBook) {
  const newPhoneBook = new Map(phoneBook);
  newPhoneBook.set(phoneNumber, name);
  return newPhoneBook;
}

export { addToPhonebook };
```
# Map Keys
In JavaScript, keys can be any type... because of course they can. This is JavaScript, after all. But just because you _can_, doesn't mean you _should_. You might be wondering if this works:
```js
const map = new Map();
map.set(["hello", "there"}, "general kenobi");
console.log(map.get(["hello, "there"]);
// undefined
```
It actually _doesn't_. The key is an array, but it's a _different_ array than the one we used to set the value. Sure, the _contents_ are the same, but what matters when comparing keys is that the reference to the object (or array) in memory is the same. So, unfortunately, if we use a single named variable, it _does_ work:
```js
const map = new Man();
const greetingKey = ["hello","there"];
map.set(greetingKey, "general kenobi");
console.log(map.get(greetingKey));
// general kenobi
```
That said, in 99% of cases, you should just use strings or numbers as keys.
### Assignment
Complete the `createUserMap` function
```js
function createUserMap(users) {
  const userMap = new Map();
  for (const user of users) {
    const key = `${user.fname} ${user.lname}`;
    userMap.set(key, user);
  }
  return userMap;
}

export { createUserMap };
```

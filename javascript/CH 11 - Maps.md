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

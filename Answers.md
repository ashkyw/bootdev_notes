```js
function createUserMap(users) {
  const map = new Map();
  for (let i = 0; i <= users.length; i++) {
    //map.set(`${users[i].fname} ${users[i].lname}`, users);
    console.log(users[i].fname);
    console.log(users[i].lname);
  }
  return map;
}

export { createUserMap };
```

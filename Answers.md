```js
const getMostRecentUser = (usernames) => {
  if (usernames == []) {
    return null;
  }
  return usernames[usernames.length-1];
};

export { getMostRecentUser };
```

# Objects
JavaScript [objects]() are an almost weirdly versatile collection type. Object literals (POJOs, or "plain old JavaScript objects") are often used to store data in key-value pairs
```js
const apple = {
  name: "Apple",
  radius: 2,
  color: "red",
}
```
You can access properties stored in an object using the `.` operator:
```js
console.log(apple.name); // prints "Apple"
console.log(apple.radius); // prints "2"
console.log(apple.color); // prints "red"
```
JavaScript objects are interesting because you'll use them the way you'd probably use a map or dictionary in other languages (simple key-value pairs),
but they can also be used for more complex things like classes & prototypes.

### Assignment
Complete the `createMessage` function:
```js
function createMessage(phoneNumber, message) {
  const messageToSend = {
    phoneNumber: phoneNumber,
    message: message,
    messageLength: message.length,
  };
  return messageToSend;
}

export { createMessage };
```
# No Colon
The `key:value` syntax is the normal way to create key-value pairs in an object, but if you want a key to have the same name as an existing variable, you can omit the colon & the value. These are the same:
```js
const radius = 2;
const color = "red";
const apple = {
  radius: radius,
  color: color,
}
```
```js
const radius = 2;
const color = "red";
const apple = {
  radius, // same as radius: radius
  color: color, // set for demonstration
}
```
# Updating Properties
You can update and **add new** keys (you'll see the words "properties" and "key" used interchangeably here) to an existing object using the `.` operator. If it exists, it's updated; if it doesn't, it's created as a new property:
```js
const apple = {
  name: "Apple",
  radius: 2,
  color: "red",
};
apple.numSeeds = 3; // new property
apple.color = "green"; // update property
// {"name":"Apple", "radius":2, "color":"green", "numSeeds":3}
```
### Assignment
Complete the `addID` function
```js
function addID(campaignRecord) {
  campaignRecord.id = `${campaignRecord.campaignName}-${campaignRecord.senderName}`;
  return campaignRecord;
}

// don't touch below this line

export { addID };
```
# Nesting Properties
Objects can contain other objects. Here's two nested object literals within the `tournament` object:
```js
const tournament = {
  refree: {
    name: "Sally",
    age: 25,
  },
  prize: {
    units: "dollars",
    value: 100,
  },
}
```
We can access the nested properties the same way by chaining: `tournament.referee.name`
```js
console.log(tournament.referee.name); // Sally
console.log(tournament.referee.value); // 100
```
### Assignment
Finish the `getCampaignCreator` function
```js
function getCampaignCreator(campaign) {
  return campaign.creator.firstName;
}

export { getCampaignCreator };
```

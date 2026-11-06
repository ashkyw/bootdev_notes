# Object Literal Types
The most useful upgrade from JavaScript to TypeScript is adding types to objects.

[Object Literal Types](https://www.typescriptlang.org/docs/handbook/2/objects.html) allows you to describe the shape of an object:
```ts
function logSaiyan(saiyan: { name: string; power: number }) {
  console.log(`${saiyan.name} has power lever: ${saiyan.power}!` );
}
```
Or, more likely, you'll define an object first:
```ts
type Saiyan = {
  name: string;
  power: number;
};

function logSaiyan(saiyan: Saiyan) {
  console.log(`${saiyan.name} has power lever: ${saiyan.power}!` );
}
```
This will make a red squiggly appear in your IDE if you misspell it in TypeScript. JavaScript won't fail until you run it
### Assignment
Fix & update `processMail`
```ts
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
};

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```

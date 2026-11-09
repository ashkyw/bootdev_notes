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
# Extra Properties
_Most of the time_, when you pass an object to a function in TypeScript, it's:
    * OK to have _more_ properties than those defined in the function's parameter type
    * Not OK to have _missing_ properties

However, when you pass an object _literal_ directly to a function, TypeScript performs what's called "excess property checking". Which means it _also_ will not allow extra properties.

For example, say we have this type:
```ts
type Spaceship = {
  name: string;
  speed: number;
};
```
and we make an object with one extra property:
```ts
const Falcon = {
  name: "Millennium Falcon",
  speed: 75,
  weapons: 4, 
};
```
We can pass this object to a function that expects a `Spaceship`:
```ts
function pilot(ship: Spaceship) {
  console.log(`Piloting ${ship.name} at ${ship.speed} light-years per hour` );
}
// this is fine
pilot(falcon);
```
But interestingly, if we pass in the same object _literal_ (no variable assignment), TypeScript will throw an error:
```ts
// Error: Object literal may only specify known properties, and 'weapons' does not exist in type 'Spaceship'.
pilot({ name: "Millennium Falcon", speed: 75, weapons: 4 });
```
_It's also worth noting that many of these kinds of rules are configurable in the [`tsconfig.json`](https://www.typescriptlang.org/tsconfig)_file_.
### Assignment
Fix the `Mail` type
```ts
export type Mail = {
  from: string;
  to: string[];
  cc: string[];
  subject: string;
  body: string;
  urgent: boolean;
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to.join(", ")}
CC: ${mail.cc.join(",")}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```
# Optional Object Properties
Optional properties can be added to an object type with the `?` operator.
```ts
type Superhero = {
  name: string;
  strength: number;
  cape?: boolean // cape is optional
};
```
That means that the type of `.cape` is actually `boolean | undefined`, just like optional function parameters
> [!TIP]
> Do _not_ go overboard using optional properties. Require all the fields that **should** be there. It will make your life easier with and you won't
> have so many runtime checks that look like this:

```ts
function fight(superhero: Superheor) {
  if (!superhero.cape) {
  // something
  }
// happy path thing
}
```
### Assignment
Fix the `Mail` type.
```ts
export type Mail = {
  from: string;
  to: string[];
  subject: string;
  body: string;
  urgent: boolean;
  cc?: string[];
};

// don't touch below this line

export function processMail(mail: Mail) {
  return `FROM: ${mail.from}
TO: ${mail.to}${!mail.cc ? "" : "\nCC: " + mail.cc}
SUBJECT: ${mail.urgent ? "[URGENT] " : ""}${mail.subject}
BODY: ${mail.body}`;
}
```

import { moo } from "./moo.js";
import { say } from "cowsay";
const name = "boot.dev";
//console.log(moo(name));
console.log(
  say(
    {
      text : moo(name),
      e : "oO",
      T : "U "
    }
  )
);

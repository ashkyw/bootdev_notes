# SnekObjects

Objects in C?!? No. Way.

However, our Sneklang is build in C, and everything in Sneklang is an "object". To be clear, not a _class_ or _object-oriented programming_ object, but a higher-level data structure that _holds some metadate about itself_.
For example:
  * What type of data it holds (int, float, string, etc.)
  * The size of the data it holds
  * The data itself
  * How many references to itself exist (at least later when we build the garbage collector)

That last item it critical. Sneklang is a garbage-collected language, we need to know how many references to an object exist so we can free it when it's no longer needed.

### Assignment
Complete the missing definitions in `snekobject.h`
* An enum called snek_object_kind_t with a single value `INTEGER`
* A union called snek_object_data_t with a single member, an integer named `v_int`
* A struct declaration called `snek_object_t` with two members:
  1. A member of type `snek_object_kind_t` named `kind`
  2. A member of type `snek_object_data_t` named `data`
```C
// End of lesson code
```

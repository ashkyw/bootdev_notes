# Handling Cycles

We built a simple reference garbage collector. It can handle:
* Simple types like `INT` and `FLOAT`
* Dynamically allocated types like `STRING`
* Static Container types, like `VECTOR3`
* Dynamic container types, like `ARRAY`

However, there's a problem with our implementation. Look at this code:
```C
snek_object_t *first = new_snek_array(1):
snek_object_t *second = new_snek_array(1):
// refcounts: first = 1, second = 1
snek_array_set(first, 0, second);
// refcounts: first = 0, second = 1
refcount_dec(second);
// refcounts: first = 0, second = 0
// all free!
```
We create a `first` array, and shove the  `second` array inside of it. Everything here works as expected. The trouble arises when we introduce a cycle: for example,  `first` contains `second`, but `second`also contains `first`...

### Assignment
Run the code in its current state. Notice that the assertions in `main.c` _fail_. Even though we decremented both the `first` and `second` arrays' refcounts, neither was freed: the refcounts are not `0`!

Fix the _assertions_ to pass by updating them to match the sad reality of our current implementation.

**Observe**

The reason both refcounts are stuck at `1` after being decremented is that, when `first` has its refcount decremented, it already has `2`. So it only drops to `1`, which does _not_ trigger a "free" of the `second` array:
```C
void refcount_dec(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount--;
  if (obj->refcount == 0) {
    // this doesn't happen when refcount is 1
    return refcount_free(obj);
  }
  return;
}
```
And because `second` still has `2` refcounts, it also only drops to `1`, which fails to trigger a "free" of the first array. In other words, we have a cycle, and our simple reference counting garbage collector can't handle it.
 **NOTE:** This assignment we just updated the unit tests to force the current implementation to work.
```C
#include "bootlib.h"
#include "munit.h"
#include "snekobject.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, correctly_free, {
  snek_object_t *first = new_snek_array(1);
  snek_object_t *second = new_snek_array(1);
  // refcounts: first = 1, second = 1
  snek_array_set(first, 0, second);
  // refcounts: first = 1, second = 2
  snek_array_set(second, 0, first);
  // refcounts: first = 2, second = 2
  refcount_dec(first);
  refcount_dec(second);
  assert_int(first->refcount, ==, 1, "Refcount first should be ?");
  assert_int(second->refcount, ==, 1, "Refcount second should be ?");
});

// Don't touch below this line

int main() {
  MunitTest tests[] = {
      munit_test("/correctly_free", correctly_free),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("refcount", tests);

  int result = munit_suite_main(&suite, NULL, 0, NULL);

  printf("*** NOTE: A memory leak warning is EXPECTED here ***\n");
  printf("*** We'll fix the circular reference problem soon ***\n");

  return result;
}

```

## Notes from boots AI

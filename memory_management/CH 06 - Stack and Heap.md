# The Stack

Remember how we said that memory is basically just a giant array of bytes with addresses at various offsets?

That's true, but it also has some additional structure. In particular, memory is divided into two main regions: the **stack** and the **heap**.

The stack is where local variables are stored. When a function is called, a new **stack frame** is created in memory to store the function's parameters and local variables. When the function returns, its entire stack frame is deallocated.

The stack is aptly named: it is a **stack** (the "Last In, First Out" data structure) of memory frames. Each time a function is called, a new frame is pushed onto the stack. When the function returns, its frame is popped off the stack.

Take a look at this example function:
```C
void create_typist(int uses_nvim)  {
  int wpm = 150;
  char name[4] = {'t','e','e','j'};
}
```
Say we call `create_typist(1)`. Before the call, our stack memory might look like this, with the next memory address to be used `0x0004`:

![Stack Memory 1](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Stack%20Memory%201.png)

Once called, the [stack pointer](https://en.wikipedia.org/wiki/Stack_pointer) is moved to make room for:
  * The [return address](https://en.wikipedia.org/wiki/Return_statement) (to pick up execution after the function returns)
  * Arguments to the function
  * Local variables in the function body

![Stack Memory 2](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Stack%20Memory%202.png)

and the local variables are stored in the stack frame:

![Stack Memory 3](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Stack%20Memory%203.png)

When the function returns, the stack frame is deallocated by resetting the stack pointer to where the frame began.
```C
// End of lesson code

#include "exercise.h"
#include <stdio.h>

int main() {
  printMessageOne();
  printMessageTwo();
  printMessageThree();
  return 0;
}

// __attribute__((noinline)) helps the compiler behave; don't worry about it
__attribute__((noinline)) void printMessageOne(void) {
  const char *message = "Dark mode?\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

__attribute__((noinline)) void printMessageTwo(void) {
  const char *message = "More like...\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

__attribute__((noinline)) void printMessageThree(void) {
  const char *message = "dark roast.\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

// don't touch below this line

void printStackPointerDiff(void) {
  static void *last_sp = NULL;
  void *current_sp;
  current_sp = __builtin_frame_address(0);
  long diff;
  if (last_sp == NULL) {
    last_sp = current_sp;
    diff = 0;
  } else {
    diff = (char *)last_sp - (char *)current_sp;
  }
  printf("---------------------------------\n");
  printf("Stack pointer offset: %ld bytes\n", diff);
  printf("---------------------------------\n");
}

```

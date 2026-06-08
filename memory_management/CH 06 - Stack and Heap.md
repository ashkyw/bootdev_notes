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
# Why a Stack?

Allocating memory on the stack is preferred when possible because the stack is faster and simpler than the heap.

  * **Efficient Pointer Management**: Stack "allocation" is just a quick increment or decrement of the stack pointer, which is extremely fast. Heap allocations require more complex bookkeeping.
  * **Cache-Friendly Memory Access**: Stack memory is stored in a contiguous block, enhancing cache performance due to spatial locality. Related values live next to each other in memory, so the CPU can load and access them more quickly.
  * **Automatic Memory Management**: Stack memory is managed automatically as functions are called and as they return.
  * **Inherent Thread Safety**: Each thread has its own stack. Heap allocations require synchronization mechanisms when used concurrently, potentially introducing overhead.

# Stack Overflow

So the stack is great and all, but one of the downsides is that it has a limited size. If you keep pushing frames onto the stack without popping them off, you'll eventually run out of memory and get a [stack overflow](https://en.wikipedia.org/wiki/Stack_overflow).

That's one of the reasons recursion without [tail-call optimization](https://en.wikipedia.org/wiki/Tail_call) can be dangerous. Each recursive call pushes a new frame onto the stack, and if you have too many recursive calls, you'll run out of stack space.
```C
#include <stdio.h>

int main() {
  const int pool_size = 1024 * 10;
  char snek_pool[pool_size];
  snek_pool[0] = 's';
  snek_pool[1] = 'n';
  snek_pool[2] = 'e';
  snek_pool[3] = 'k';
  snek_pool[4] = '\0';

  printf("Size of pool: %d\n", pool_size);
  printf("Initial string: %s\n", snek_pool);
  return 0;
}
```

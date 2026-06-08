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

# Pointers to the Stack

So we know that stack frames are always getting pushed and popped, and as a result, memory addresses on the stack are always changing and getting refused.

_Remeber: the stack is only safe to use within the context of the current function!_
```C
// End of lesson code

#include <stdio.h>

typedef struct {
  int x;
  int y;
} coord_t;

__attribute__((noinline))

// Don't touch above this line

coord_t new_coord(int x, int y) {
  coord_t c;
  c.x = x;
  c.y = y;
  return c;
}

int main() {
  coord_t c1 = new_coord(10, 20);
  coord_t c2 = new_coord(30, 40);
  coord_t c3 = new_coord(50, 60);

  printf("c1: %d, %d\n", c1.x, c1.y);
  printf("c2: %d, %d\n", c2.x, c2.y);
  printf("c3: %d, %d\n", c3.x, c3.y);
}
```
# The Heap

## ![Video notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/best-place-to-store-in-memory-data-1920x1080.mp4)

The stack is _simpler_ and _faster_, but is a bit **more limited**.

The heap is _slower_ and a bit **more complex** to work with, but it allows us to create more sophisticated and complicated data structures.

## Stack Frames

You get a new stack frame every time you call a function. Each stack frame has a stack pointer, showing us where we are in case another function requires a new frame. The first address in the frame is reserved for the return address. The next address is reserved to **copy** any arguments required for the function. Next is the int type within that function. Then each char of a string. Each time the stack pointer increments along the frame, pointing out where it currently is in memory. After the function executes, the stack pointer moves back to the return address, effectively freeing the memory used in the function. 

## The Heap
 
Much slower because we need to dynamically allocate this memory, and grab new resources from the operating system. It's more complex because it is possible to forget to free that memory, causing memory leaks, and possible running out of memory entirely.

Why do we use the heap if all this can happen? Well, we don't always know how much memory we'll need ahead of time. 

### Rule of thumb

  * **Stack** - Used when the size is _known_ ahead of time and can exist within _one_ function.
  * **Heap** - Used when the size is ***unknown*** ahead of time, or a return value is _not_ limited to one function.

## Lesson notes

["The heap"](https://en.wikipedia.org/wiki/Memory_management#Dynamic_memory_allocation), as opposed to "the stack", is a pool of long-lived memory shared across the entire program. Stack memory is automatically allocated and deallocated as functions are called and returned, but heap memory is allocated and deallocated as needed, independent of the burdensome shackles of function calls.

When you need to store data that outlives the function that created it, you'll send it to the heap. The heap is called "dynamic memory" because it's allocated and deallocated as needed. Take a look at `new_int_array`:
```C
int *new_int_array(int size) {
  int *new_arr = malloc(size * sizeof(int)); // Allocate memory
  if (new_arr == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1); // Exit if allocation fails
  }
  return new_arr;
}
```
Because the size of the array isn't known at compile time, we can't put it on the stack. Instead, we allocate memory using the `<stdlib.h>`'s `[malloc](https://en.cppreference.com/w/c/memory/malloc)` function. It takes a number of bytes to allocate as an argument (`size * sizeof(int)`) and returns a pointer to the allocated memory (a `void *` that is automatically converted to an `int *` when assigned). Here's a diagram of what happened in memory:
![The Heap 1](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/The%20Heap%201.png)
The `new_int_array` function's `size` argument is just an integer, it's pushed onto the stack. Assuming `size` is `6`, when `malloc` is called we're given enough memory to store 6 integers on the heap, and we're given the address of the start of that newly allocated memory. We store it in a new local variable called `new_arr`. The address is stored on the stack, but the data it points to is in the heap.

Let's look at some code that uses `new_int_array`:
```C
int* arr_of_6[0] = 69;
int* arr_of_6[1] = 42;
int* arr_of_6[2] = 420;
int* arr_of_6[3] = 1337;
int* arr_of_6[4] = 7;
int* arr_of_6[5] = 0;
```
The data is stored in the heap:
![The Heap 2](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/The%20Heap%202.png)
When we're done with the memory, we need to manually deallocate it using the `<stdlib.h>`'s [`free`](https://en.cppreference.com/w/c/memory/free) function:
```C
free(arr_of_6);
```
![The Heap 3](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/The%20Heap%203.png)

The `free` function returns (deallocates) that memory for use elsewhere. It's important to note that the pointer (`arr_of_6`) still exists, but shouldn't be used. It's a "dangling pointer", pointing to deallocated memory.
```C
// End of lesson code


```

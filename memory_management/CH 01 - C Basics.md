# Welcome to Memory Management

Understanding how your _software_ runs on _hardware_ is important for writing fast, performant code. In this course we'll be talking all about one of the main aspects of software performance: **memory management**.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  printf("Starting the Sneklang interpreter...\n");
  return 0;
}
```

## C Program Structure

In python you do something like this:

```py
python slow_program.py
```

The Python interperter then executes the file top-to-bottom. If you have a `print()` at the top level, then it will print something.

The entire file is _interpreted line by line, but that's not how C works_.

### The simplest C Program:

The simplest C program is essentially:

```C
int main() {
  return 0;
}
```

But a lot is happening here....

  * A function named `main` is _always_ the entry point to a C program (unlike Python, which enters at the top of the file).
  * `int` is the return type of the function and is short for "integer". Because this is the `main` function, the return value is the [exit code](https://en.wikipedia.org/wiki/Exit_status) of the program. `0` means success, anything else means failure.
      * You"ll find a lot of abbreviations in C because 1) programmers are lazy, and 2) it used to matter how many bytes your source code was.
  * The openinig bracket, `{` is the start of the function's body (C ignores whitespace, so indentation is just for style, not for syntax)
  * `return 0` returns the `0` value (an integer) from the function. Again, this is the exit code because it's the `main` function.
      * `0` reprsents "nothing bad happened" as a return value
  * The pesky `;` is required in C to terminate statements.
  * The closing bracket, `}` denotes the end of the function's body.

## Print

It feels very different coming from Python, but printing in C is done with a function called `printf` from the [stdio.h](https://www.ibm.com/docs/en/zos/2.4.0?topic=files-stdioh-standard-input-output) (standard input/output) library with a lot of weird formatting rules. To use it, you need an `#include`at the top of your file:

```C
#include <stdio.h>
```

Then you can use [printf](https://devdocs.io/c/io/fprintf) for inside a function:

```C
printf("Hello, world!\n");
```

_Notice the `\n`: it's required to print a_ [newline character](https://en.wikipedia.org/wiki/Newline) _(and flush the buffer in the browser), which `print()` in Python does automatically._

_In case you're wondering, the `f` in `printf` stands for "print formatted"._

```C
// End of lesson code:
#include <stdio.h>

int main() {
  printf("Program in C!");
  return 0;
}
```

# C is compiled

This Python code prints "starting" _before_ it crashes:

```py
print("starting")
func_that_doesnt_exist("uh oh")
print("finished")
```

But in C, it crashes _before it can even run_. If's there's a problem, the compiler tells us before the program even starts.

Now... C doesn't tell us about all the possible problems (read: skill issue) that might arise in our program. But it does tell us about _some_ of them.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  printf("starting sneklang tools\n");
  printf("finished sneklang tools\n");
  return 0;
}
```

## Comments

There are two ways to write comments:

```C
// This is a single-line comment

/*
This is a multi-line commment
I can just keep adding lines
and it will still be a comment
*/
```

`/*` and `*/` are used to denote the beginning and end of a multi-line comment.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  /*
    Sneklang is for nvim enjoyers
    who want to write their own garbage
    collectors instead of using off-the-shelf
    solutions
  */
  printf("i use sneklang btw\n");
  printf("i use nvim btw\n");
  printf("i use arch btw\n");
  return 0;
}

```

## Basic Types

* `int` - An integer
* `float` - A floating point number
* `char` - A character
* `char *` - An array of charcters (more on this later... If you think about it, sounds kinda like a string, doesn't it?)

You've already seen `int` in previous examples - it's the return value in the special `main` function (the entry point for every C program).

When declaring a variable, you must specify its type before the main and assigning a value.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  int max_recursive_calls = 100;
  char io_mode = 'w';
  float throttle_speed = 0.2;

  // don't touch below this line
  printf("Max recursive calls: %d\n", max_recursive_calls);
  printf("IO mode: %c\n", io_mode);
  printf("Throttle speed: %f\n", throttle_speed);
  return 0;
}
```

### Strings

 Most programming languages these days (even compiled ones) have a built-in `string` type of some sort. C... doesn't.

 Instead, C strings are just arrays (like lists) of characters. More about the specifics of arrays and pointers later. For now, this is just how you get a string in C.

```C
char *msg_from_dax = "You still have 0 users";
```

Very (repeat: **_VERY_**) loosely speaking, `char *` means string. Note, it is required to use `"`. Single quotes (`'`) make `char`, not `char *`.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  char *will_never_hear_again =
      "Hey TJ, when is the memory course in C gonna be done?";

  // don't touch below this line
  printf("%s\n", will_never_hear_again);
  return 0;
}
```

## Printing variables

You've seen `printf()` magic a few times. Unfortunately, in C it isn't as easy to do string interpolation (f-strings in Python).

Instead of:

```py
print(f"Hello, {name}. You're {age} years old.")
```

We have to tell C _how_ we want particular values to be printed using "format specifiers."

Common [format specifiers](https://cplusplus.com/reference/cstdio/printf/#:~:text=Parameters-,format,-C%20string%20that) are:

* `%d` - digit (integer)
* `%c` - character
* `%f` - floating point number
* `%s` - string (char *)

```C
printf("Hello, %s. You're %d years old. \n", name, age);
```

### Newline Character

The `print()` function in Python automatically adds a !(newline character)[https://en.wikipedia.org/wiki/Newline] (`\n`) at the end of the string. In C, we have to do this manually.

```C
printf("Hello, world!\n")
```

```C
// End of lesson code:
#include <stdio.h>

int main() {
  int sneklang_default_max_threads = 8;
  char sneklang_default_perms = 'r';
  float sneklang_default_pi = 3.141592;
  char *sneklang_title = "Sneklang";
  // don't touch above this line

  printf("Default max threads: %d\n", sneklang_default_max_threads);
  printf("Custom perms: %c\n", sneklang_default_perms);
  printf("Constant pi value: %f\n", sneklang_default_pi);
  printf("Sneklang title: %s\n", sneklang_title);
  return 0;
}
```

## Compilation Types

You're probably familiar with the idea of `types` from Python, but C does them quite a bit differently.

In Python it's OK (but still disgusting) to change the type of a variable:

```py
x = 12345
x = "Wow, a new type"
x = False
x = None
x = "ok a string again :'("
```

In C, changing the type of an existing variable is not allowed:

```C
int main() {
  char *max_threads = "5";

  // call badcop
  // this is illegal
  max_threads = 5;
}
```

## Variables

As we talked about, variables cannot change types:

```C
int main() {
  int x = 5;
  float x = 3.14; // error
}
```

However, a variable's _value_ can change:

```C
int main() {
  int x = 5;
  x = 10; // this is ok
  x = 15; // still ok
}
```
When updating a variable's value, you do not need to redeclare the type. In fact, you can't.

```C
// End of lesson code:
#include <stdio.h>

int main() {
  int sneklang_int_size = 64;
  sneklang_int_size = 32;
  printf("Sneklang int size: %d bits\n", sneklang_int_size);
  return 0;
}
```

## Constants

So a variable's _value_ can change:

```C
int main() {
  int x = 5:
  x = 10: // this is ok
}
```

But what if we want to create a value that _can't_ change? We can use the [const type qualifier](https://en.cppreference.com/w/c/language/const).

```C
int main() {
  const int x = 5;
  x = 10; // error
}
```

# Functions

In C, functions specify the types for their arguments and return value.

```C
float add(int x, int y) {
  return (float)(x+y);
}
```
* The first type, `float` is the return type.
* `add` is the name of the function.
* `int x + y` are the parameters to the function, and their types are specified.
* `x + y` adds the two arguments together.
* `(float)` casts the result to a float.
  * We'll talk more about what [cast](https://en.wikipedia.org/wiki/Type_conversion) means later, and the rules for casting to and from certain types.
  * The simple verison is that it instructs C to convert the result of `x + y` to a `float` value.

Here's how you would call this function:

```C
int main() {
  float result = add(10, 5);
  printf("result: %f\n", result);
  // result: 15.000000
  return 0;
}
```

It's nice that C functions enforce returning the same type from all return statements, isn't it? In Python, it can be a pain to realize that a function returns different types depending on the path it took.

```C
// End of lesson code:
#include <stdio.h>

int max_sneklang_memory(int max_threads, int memory_per_thread) {
  return max_threads * memory_per_thread;
}

// don't touch below this line

void init_sneklang(int max_threads, int memory_per_thread) {
  printf("Initializing Sneklang\n");
  printf("Max threads: %d\n", max_threads);
  printf("Memory per thread: %d\n", memory_per_thread);
  int max_memory = max_sneklang_memory(max_threads, memory_per_thread);
  printf("Max memory: %d\n", max_memory);
  printf("====================================\n");
}

int main() {
  init_sneklang(4, 512);
  init_sneklang(8, 1024);
  init_sneklang(16, 2048);
  return 0;
}
```

# Void

In C, there's a special type for function signatures: [`void`](https://en.wikipedia.org/wiki/Void_type). There are two primary ways you'll use `void`:

To explicitly state that a function takes no arguments:

```C
int get_integer(void) {
  return 42;
}
```

When a function doesn't return anything:

```C
void print_integer(int x) {
  printf("this is an int %d", x)
}
```

It's important to note that `void` in C is **_not_** like `None` in Python. It's not a value that can be assigned to a variable. _It's just a way to say that a function doesn't return anything or doesn't take any arguments._

## Math Operators

All the same operators you'd expect exist in C:

```C
x + y;
x - y;
x * y;
x / y;
```

Coming from Python `+=`,`-=`,`*=`,`/=` are all the same.

In addition, there are also [`++` and `--` operators](https://en.cppreference.com/w/cpp/language/operator_incdec):

```C
x++; // += 1
x--; // -= 1
```
_The name of C++ is a bit of a joke by the creator, it's meant to be "incremented C" or "better C"._

These increment (`++`) and decrement (`--`) operators can be used in two forms: postfix and prefix.

**Postfix (`x++` or `x--`)**: The value of `x` is used in the expression first, and then `x` is incremented or decremented. For example:

```C
int a = 5;
int b = a++; // b is assigned to 5, then a becomes 6
```

**Prefix (`++x` or `--x`)**: `x` is incremented or decremented first, and then the new value of `x` is used in the expression. For example:

```C
int a = 5;
int b = ++a // a becomes 6, then is assigned to b
```
> [!Note]
> Avoid Prefix. Postfix is more common, especially in loops.

```C
// End of lesson code:
float snek_score(int num_files, int num_contributors, int num_commits,
                 float avg_bug_criticality) {
  int project_size = num_files * num_commits;
  int project_complexity = project_size + num_contributors;
  return (float)project_complexity * avg_bug_criticality;
}
```

# If statements

`if` statements are the most basic form of control flow in C: very similar to other languages. Basic syntax:

```C
if (x > 3) {
  printf("x is greater than 3\n");
}
```

`if`/`else`/`else if` are also available:

```C
if (x > 3) {
  printf("x is greater than 3\n");
} else if (x == 3) {
  printf("x is equal to 3\n");
} else {
  printf("x is less than 3\n");
}
```

### Janky syntax

You _can_ write an `if` statement without braces is you only have one statement in the body:

```C
if (x > 3) printf("x is greater than 3\n");
```

> [!Warning]
> This is C. It's known for providing a myriad of ways to shoot yourself in the foot. It's easy to mess up, don't use this syntax.

```C
// End of lesson code:

#include "exercise.h"

char *get_temperature_status(int temp) {
  if (temp < 70) {
    return "too cold";
  } else if (temp > 90) {
    return "too hot";
  } else {
    return "just right";
  }
}
```

# Logical Operators

Logical operators let you combine multiple conditions in C. There are three main logical operators you'll use all the time:

* `&&` - Logical `AND`: true if _both_ conditions are true
* `||` - Logical `OR`: true if _either_ conditions is true
* `!` - Logical `NOT`: inverts a boolean value

```C
int age = 25;
bool has_license = true;

if (age >= 18 && has_license) {
  printf("Can drive \n");
}
```

### Short-Circuit Evaluation

C uses short-circuit evaluation with logical operators. This means:
  * With `&&`, if the first condition is false, the second isn't even checked (because the whole thing is already false)
  * With `||`, if the first condition is true, the second isn't even checked (because the whole thing is already true)

```C
if (x != 0 && 10 / x > 2) {
  // The divison only happens if x != 0
  // This prevents a divison by zero error
  printf("Safe!\n")
}
```

## Operator Precedence

Logical NOT (`!`) has higher precedence than AND (`&&`), which has higher precedence than OR (`||`). When in doubt, use parentheses to make your intent crystal clear:

```C
// without parentheses - might be confusing
if (!is_raining && is_sunny || is_weekend)

// with parentheses - much clearer
if ((!is_raining && is_sunny) || is_weekend)
```

```C
// End of lesson code:
#include "exercise.h"

int can_access_registry(int is_premium, int reputation, int has_2fa){
  if ((is_premium == 1) || (reputation >= 100 && has_2fa)){
    return 1;
  } else {
    return 0;
  }
}

```

> [Note]
> In C we use `1` for true and `0` for false when returning boolean-like values from functions that return `int`.

# Ternary

Like Javascript, C has a ternary operator:

```C
int a = 5;
int b = 10;
int max = a > b ? a : b;
printf("max: %d\n", max);
// max: 10
```
Let's break down this syntax:

```C
a > b ? a : b
```
* `a > b` is the condition
* `?` begins the "then" value
* `a` is the final value is the condition is true
* `:` separates the "else" value
* `b` is the final value is the condition is false
* The entire expression (`a > b ? a : b`) evaluates to either `a` or `b`, which is then assigned to `max` in the example.

_Ternaries are a way to write simple if/else statements in one line_

# Type sizes

In C, the "size" (in memory) of a type is not guaranteed to be the same on all systems. That's because the size of a type is dependent on the system's architecture. 
For example, on a 32-bit system, the size of an `int` is usually 4 bytes, while on a 64-bit system, the size of an `int` can sometimes be 8 bytes - of course, you never know until you run `sizeof` with the compilier.

However, some types are always guaranteed to be the same. Here's a list of the basic C data types along with their typical sizes in bytes. Note that sizes can vary based on the platform (e.g. 32-bit vs. 64-bit systems):

###### Basic C types and sizes

* `char`
  * Size: **1 byte**
  * Represents: **single character**
  * Notes: **Always 1 byte, but can be signed or unsigned**
    
* `float`
  * Size: **4 bytes**
  * Represents: **Single-precision floating-point number**
     
* `double`
  * Size: **8 bytes**
  * Represents: **Double-precision floating-point number**

The actual sizes of these types can be deteremined using the `sizeof` operator in C for a specific platform.

## Sizeof

C gives us a way to check the size of a type or a variable: [sizeof](https://en.cppreference.com/w/c/language/sizeof).

You can use `sizeof` like a function (although, technically it's a [`unary operator`](https://en.wikipedia.org/wiki/Unary_operation), but that distincstion is generally only useful for winning _super important_ internet arguments).

We'll use the `sizeof` operator in the next few lessons to give us insight into the memory layout of different types in C. This will be particularly useful as we move deeper into C, and **_essential_** for understanding pointers.

### **`size_t`**

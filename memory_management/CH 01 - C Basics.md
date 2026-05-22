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
  * `int` is the return type of the function and is short for "integer". Because this is the `main` function, the return value is the ![exit code](https://en.wikipedia.org/wiki/Exit_status) of the program. `0` means success, anything else means failure.
      * You"ll find a lot of abbreviations in C because 1) programmers are lazy, and 2) it used to matter how many bytes your source code was.
  * The openinig bracket, `{` is the start of the function's body (C ignores whitespace, so indentation is just for style, not for syntax)
  * `return 0` returns the `0` value (an integer) from the function. Again, this is the exit code because it's the `main` function.
      * `0` reprsents "nothing bad happened" as a return value
  * The pesky `;` is required in C to terminate statements.
  * The closing bracket, `}` denotes the end of the function's body.

## Print

It feels very different coming from Python, but printing in C is done with a function called `printf` from the ![stdio.h](https://www.ibm.com/docs/en/zos/2.4.0?topic=files-stdioh-standard-input-output) (standard input/output) library with a lot of weird formatting rules. To use it, you need an `#include`at the top of your file:

```C
#include <stdio.h>
```

Then you can use ![printf](https://devdocs.io/c/io/fprintf) for inside a function:

```C
printf("Hello, world!\n");
```

_Notice the `\n`: it's required to print a ![newline character](https://en.wikipedia.org/wiki/Newline) (and flush the buffer in the browser), which `print()` in Python does automatically._

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

You've seen `printf` magic a few times. 

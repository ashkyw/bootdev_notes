# Enums

C has explicit support for `enum`s (enumerations) with the [`enum` keyword](https://en.cppreference.com/w/c/language/enum).

You can define a new enum type like this:
```C
typedef enum DaysOfWeek {
  MONDAY,
  TACO_TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  FUNDAY
} days_of_week_t; 
```
The `typedef` and its alias `days_of_week_t` are optional, but like with structs, they make the enum eaiser to use.

In the above example, `days_of_week_t` is a new type that can _only_ have one of the values defined in the `enum`:

  * `MONDAY`, which is 0
  * `TACO_TUESDAY`, which is 1
  * `WEDNESDAY`, which is 2
  * `THURSDAY`, which is 3
  * `FRIDAY`, which is 4
  * `SATURDAY`, which is 5
  * `FUNDAY`, which is 6

You can use the enum type like this:
```C
typedef struct Event {
  char *title;
  days_of_week_t day;
} event_t;

// Or if you don't want to use the alias:

typedef struct Event {
  char *title;
  enum DaysOfWeek day;
} event_t;
```

An `enum` is _not_ a collection type like a struct or an array. It's just a list of intgers constrained to a new type, where each is given an explicit name.
```C
// End of lesson code

typedef enum Color {
  RED,
  GREEN,
  BLUE,
} color_t;
```
# Non-Default Values

Sometimes, you don't just want to enumerate some _names_ (where underlying integer constant values don't really matter) you want to set those enumerations to _specific_ values. For example, you might want to define a program's [exit status codes](https://en.wikipedia.org/wiki/Exit_status):
```C
typedef enum {
  EXIT_SUCCESS = 0,
  EXIT_FAILURE = 1,
  EXIT_COMMAND_NOT_FOUND = 127,
} ExitStatus;
```
Alternatively, you can define the first value and let the compilire fill in the rest (incrementing by 1):
```C
typedef enum {
  LANE_WPM = 200,
  PRIME_WPM, // 201,
  TEEJ_WPM, // 202
} WordsPerMinute;
```
```C
// End of lesson code:
typedef enum Color {
  RED = 55,
  GREEN = 176,
  BLUE = 38
} color_t;
```
# Switch Case

One of the best features of `enums` is that it can be used in [`switch` statements](https://en.cppreference.com/w/c/language/switch). Enums + switch statements:
  * Avoid "[magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming))"
  * Use descriptive names
  * With modern tooling, will give an error/warning that you haven't handled all the cases in your switch

```C
switch (logLevel) {
  case LOG_DEBUG:
    printf("Debug logging enabled\n");
    break;
  case LOG_INFO:
    printf("Info logging enabled\n");
    break;
  case LOG_WARN:
    printf("Warning logging enabled\n");
    break;
  case LOG_ERROR:
    printf("Error logging enabled\n");
    break;
  default:
    printf("Unknown log level: %d\n", logLevel);
    break;
}
```

You'll notice that we have a `break` after each case. If you do **not** have a `break` (or `return`), the next case will _still execute_: it "falls through" to the next case. Many devs have written bugs when using switch statements, because they forgot to add `break`. 

In some rare cases, you might want the fallthrough:

```C
switch (errorCode) {
  case 1:
  case 2:
  case 3:
    // 1, 2, and 3 are all minor errors
    printf("Minor error occurred. Please try again.\n");
    break;
  case 4:
  case 5:
    // 4 and 5 are major errors
    printf("Major error occurred. Restart required.\n");
    break;
  default:
    printf("Unknown error.\n");
    break;
}
```

But usually this is a footgun. You'll almost always want a `break` at the end of each case statement.

```C
// End of lesson code
#include "http.h"

char *http_to_str(http_error_code_t code) {
  switch (code) {
  case HTTP_BAD_REQUEST:
    return "400 Bad Request";
  case HTTP_UNAUTHORIZED:
    return "401 Unauthorized";
  case HTTP_NOT_FOUND:
    return "404 Not Found";
  case HTTP_TEAPOT:
    return "418 I AM A TEAPOT!";
  case HTTP_INTERNAL_SERVER_ERROR:
    return "500 Internal Server Error";
  default:
    return "Unknown HTTP status code";
```

# Sizeof Enum

The same `sizeof` operator that we've discussed works on enums.

Generally, enums in C are the same size as an `int`. However, if an enum value exceeds the range of an `int`, the C compiler will use a [larger integer type](https://en.cppreference.com/w/c/language/type) to accomodate the value, such as `unsigned int` or `long`.
  * [`unsigned int`](https://en.wikipedia.org/wiki/C_data_types#:~:text=unsigned-,unsigned%20int,-Basic%20unsigned%20integer) doesn't represent negative numbers, so it can represent larger positive numbers.
  * [`long`](https://en.wikipedia.org/wiki/C_data_types#:~:text=%5B8%5D-,long,-long%20int) is just a larger integer type than `int`, so it can represent larger numbers.

### Just Fancy Integers

Enums are often used to represent the possibilities in a set. For example:
  
  * `SMALL` = 0
  * `MEDIUM` = 1
  * `LARGE` = 2
  * `EXTRA_LARGE` = 3

Your code probably cares a lot about _which size_ a variable represents, but it probably doesn't care that `SMALL` happens to be `0` under the hood. From the compiler's perspective, enums are just fancy numbers.

```C
// End of lesson code

#include <stdio.h>

typedef enum {
  BIG = 123412341234,
  BIGGER,
  BIGGEST,
} BigNumbers;

typedef enum {
  HTTP_BAD_REQUEST = 400,
  HTTP_UNAUTHORIZED = 401,
  HTTP_NOT_FOUND = 404,
  HTTP_I_AM_A_TEAPOT = 418,
  HTTP_INTERNAL_SERVER_ERROR = 500
} HttpErrorCode;

int main() {
  printf("The size of BigNumbers is %zu bytes\n", sizeof(BigNumbers));
  printf("The size of HttpErrorCode is %zu bytes\n", sizeof(HttpErrorCode));
  return 0;
}
```
```C
// End of lesson .c file
#include "exercise.h"
#include <stdio.h>

void format_object(snek_object_t obj, char *buffer) {
  switch (obj.kind) {
  case INTEGER:
    sprintf(buffer, "int:%d", obj.data.v_int);
    break;
  case STRING:
    sprintf(buffer, "string:%s", obj.data.v_string);
    break;
  }
}

// don't touch below this line

snek_object_t new_integer(int i) {
  return (snek_object_t){
      .kind = INTEGER,
      .data = {.v_int = i},
  };
}

snek_object_t new_string(char *str) {
  // NOTE: We will learn how to copy this data later.
  return (snek_object_t){
      .kind = STRING,
      .data = {.v_string = str},
  };
}

// End of lesson .h file
typedef enum SnekObjectKind {
  INTEGER,
  STRING,
} snek_object_kind_t;

// don't touch below this line

typedef union SnekObjectData {
  int v_int;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t new_integer(int);
snek_object_t new_string(char *str);
void format_object(snek_object_t obj, char *buffer);
```

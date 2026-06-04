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

```

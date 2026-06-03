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

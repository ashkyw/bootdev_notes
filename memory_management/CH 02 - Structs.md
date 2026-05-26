# Structs

##### [Video notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/what-are-structs-1920x1080.mp4)

Structs in C are similar to objects & classes in other languages, but simpler. There's no concepts of inheritance, class methods, or static variables.
Instead, they are simply a way to group multiple fields or data points and put them all into one _object_. This way they can be moved around and stored together.

Instead of typing numerous variables for a function, we can logically group them into a struct and pass them around together. 
Much like how classes in Python group things together. 

Structs do not have any behavior, they are simply just data.

Struct fields can be accessed with the `.` operator. If you have a pointer, it can be accessed with the `->` operator.

One difference between structs and classes is that the declaration order matters. This determines the size and layout of memory for the struct.

When we make a struct what we're doing is telling C that we have several different pieces of data that we want grouped together in memory, so we can operate on that memory as a block. That block can be bigger or smaller depending on how we lay out the data.

##### Lesson Notes

So far all we've seen are the _simple_ (non-collection) types in C. However, stuff like this can get really annoying:
```C
int main() {
    int x_1 = 1;
    int y_1 = 2;
    int z_1 = 3;
    int x_2 = 4;
    int y_2 = 5;
    int z_2 = 6;

    int dist = distance(x_1, y_1, z_1, x_2, y_2, z_2);
    printf("Distance: %d", dist);
}
```
Because our distance function starts to look... ridiculous.
```C
int distance(int x_1, int y_1, int z_1,
             int x_2, int y_2, int z_2)
{
    // a lot of numbers
}
```
We also run into a new problem: _In C, we're only allowed to return a single value from a function_. This doesn't work:

```C
int int int scale_coordinate(int x, int y, int z, int scale) {
    return x * scale, y * scale, z * scale;
    // Error! Too many values to return
}
```
_[Structs](https://en.cppreference.com/w/c/language/struct) solve this_. Here's an example of the syntax:
```C
struct Human {
    int age;
    char *name;
    int is_alive;
};
```

```C
// End of lesson code

#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};
```

# Initializers

So now you're probably wondering: "How do we actually _make an instance of_ a struct"? You may have noticed in the previous lesson all we did was _define the struct type_.

Unfortunately, there are a few different ways to [initialize a struct](https://en.cppreference.com/w/c/language/struct_initialization), The following examples will be using this struct.

```C
struct City {
  char *name;
  int lat;
  int lon;
};
```
## Zero Initializer
```C
int main() {
  struct City c = {0};
}
```
This sets all the fields to `0` values.

## Positional Initializer

```C
int main() {
  struct City c = {"San Francisco", 37, -122};
}
```

### Designated Initializer

This is generally the preferred way to initialize a struct.

  * It's easier to read (has the field names)
  * If the fields change, you don't have to worry about breaking the ordering
```C
int main() {
  struct City c = {
    .name = "San Francisco",
    .lat = 37,
    .lon = -122
  };
}
```

Remember, it's `.name` not `name`. If this trips you up, just remember it's `.name` and not `name` because that's how you access the field, e.g. `c.name`.

 ### Accessing Fields

Accessing a field in a struct is done using the `.` operator. For example:

```C
struct City c;
c.lat = 41; // Set the latitude
printf("Latitude: %d", c.lat); // Print the latitude
```

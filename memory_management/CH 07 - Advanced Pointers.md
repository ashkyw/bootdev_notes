# Pointer-Pointers

### ![Video Notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Pointer-Pointers-V3-1920x1080.mp4).

Essentially a pointer-pointer is a variable that points to an address, that happens to be an address itself.
```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;

  int *ptr = &v1;
  int **ptr_ptr = &ptr;
  checkpoint = **ptr_ptr;

  ptr = &v2;
  checkpoint = **ptr_ptr;
}
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v1 | 0x08 | 2 |

### Lesson notes

Well, we know what a pointer is. So let's re-learn it! A pointer-to-pointer is just a pointer variable that holds the address of another pointer!

This allows you to create complex data structures like arrays of pointers, and to modify pointers indirectly. The syntax is exactly what you would expect:
```C
int value;
int *pointer;
int **pointer_pointer;
```
Pointers to pointers (or pointers to pointers to pointers) are like a treasure map or a scavenger hunt. You start at one pointer and keep following the chain of addresses until you get to the final value. It's just a chain of dereferences.

![Pointers to pointers to pointers](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Pointer%20to%20pointer%20to%20pointer.png)

# Pointer-Pointers

### ![Video Notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Pointer-Pointers-V3-1920x1080.mp4).

Essentially a pointer-pointer is a variable that points to an address, that happens to be an address itself.

We start with
```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 0 |

Next we create a pointer that points to v1, and the value becomes 0x04, the address of v1

```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;

  int *ptr = &v1;
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 0 |
| ptr | 0x20 | 0x04 |

Then we create ptr_ptr, set it to the address of v1 and it's value becomes 0x20, the address of ptr

```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;

  int *ptr = &v1;
  int **ptr_ptr = &ptr;
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 1 |
| ptr | 0x20 | 0x04 |
| ptr_ptr | 0x28 | 0x20 |

Next we set checkpoint to the pointer of ptr_ptr. It's value then becomes 1, because we are routing through the address values to get to the initial value.

```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;

  int *ptr = &v1;
  int **ptr_ptr = &ptr;
  checkpoint = **ptr_ptr;
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 1 |
| ptr | 0x20 | 0x04 |
| ptr_ptr | 0x28 | 0x20 |

Next we set ptr to the address of v2, which changes its value to 0x08, the address for v2

```C
int main () {
  int v1 = 1;
  int v2 = 2;
  int checkpoint = 0;

  int *ptr = &v1;
  int **ptr_ptr = &ptr;
  checkpoint = **ptr_ptr;

  ptr = &v2;
```
| Name | Address | Value |
|:--------:|:--------:|:--------:|
| v1 | 0x04 | 1 |
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 1 |
| ptr | 0x20 | 0x08 |
| ptr_ptr | 0x28 | 0x20 |

Finally, we set checkpoint to ptr_ptr, it's value becomes 2, because we are routing through the address values to get to the initial value.

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
| v2 | 0x08 | 2 |
| checkpoint | 0x12 | 2 |
| ptr | 0x20 | 0x08 |
| ptr_ptr | 0x28 | 0x20 |

Everything we used before with pointers works the exact same way with pointer-pointers

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
```C
// End of lesson code


```

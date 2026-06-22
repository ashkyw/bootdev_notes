# Garbage Collector

## [Video Notes](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/garbage-collection-1920x1080.mp4)

There are different kinds of garbage collectors.
#### Reference Counting
Possibly the simplest version. With this, it adds an additional field to each object that is it's count
```C
typedef struct Object {
  object_kind_t kind;
  object_kind_t data;
  object_kind_t refcount;
} object_t;
```
With this, every time an object is created or referenced the refcount increments.
```py
foo = 42 #refcount: 1
list = [foo] #refcount: 2
pop(list(foo)) #refcount: 1
```
If an object is no longer in use, the refcount decrements. Once the refcount is `0`, that memory is returned to the OS.

Reference Counting lacks the ability to track cycles. It's also expensive because everytime we do an operation, we need to modify all other objects it touches. Once that's done, we can then determine everything that is directly referenced and indirectly referenced. Any variables that aren't marked can then return that memory to the OS. 

#### Mark and Sweep
The idea that we can find all of the variable that are directly referenced by our stack frames. Then we trace through all of connections that are referenced by their roots. Any thing not referenced can be returned to the OS.

This is more complex. But it can handle cases that just reference counting can't, like a list that references another list, that references back to the original list (this is known as a cycle). 

Mark and sweep doesn't require us to do operations _every single time_ we touch or reference a variable. Work only needs to be done when we perform a "GC Pause" (garbage collector pause) which is when the GC goes and checks which variables are still alive.

## Lesson notes

A garbage collector is a program (or part of a program) that automatically frees memory thet is no longer in use. Languages like Python, Java, Javascript, OCaml, and even Go use garbage collectors _as the code is running_ to manage memory.
It's "automatic memory management." Automatic memory management can be a huge productivity boost for devs (less code, possibli fewer memory-related bugs) but it typically comes with a performance cost because the garbage collector is always running.
It's not coincedence that C, C++, Rust and Zig are all great choices when you need to squeeze every last drop of performance.

Ultimately, there is a cost with memory, the question is where do you want to pay it? In dev time, or runtime?

# Refcounting

One of the simplest ways to implement a garbage collecot is to use a [reference counting]() algorithm. It goes something like this:
  
  * All objects keep track of a `reference_count` integer.
  * When that object is referenced, its reference count is incremented.
  * When an object is garbage collected, the reference count of any object it references is decremented.
  * When any object's reference count reaches zero, the object is garbage collected.

### Assignment


## Notes from boots AI

# ![Stacks](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/stacks-1920x1080.mp4)

A [stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) is a data structure that stores ordered items. It's *like* a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack.

It's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates. It's easy to take an time off the *top* of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. You'll opten hear a stack referred to as a `LIFO` (last in, first out) data structure.

### Examples of Stacks:
  
  1. Undo & Redo functions
  2. Browser Back and Forward

### Stack Speed

You might be wondering, "why would I use a stack instead of a list?" or "Isn't this just a list with fewer features?"

And you'd be right! A stack is a list with fewer features, but that's the point. By restricting the ways we can interact with the data, we guarantee that certain operations are blazingly fast. Here are all the operations a typical stack supports, along with their Big O time complexity:

|Operation|Big O|Description|
|---------|-----|-----------|
|push 	  |O(1) |	Add an item to the top of the stack |
|pop 	    |O(1) |	Remove and return the top item from the stack |
|peek 	  |O(1) |	Return the top item from the stack without modifying the stack |
|size 	  |O(1) |	Return the number of items in the stack 

* All supported operations are `O(1)` by themselves. However, some tasks, like getting to an item at the bottom of the stack have a higher time complexity because they require multiple `pop` operations.
* Stack operations are limited: no searching, no sorting, no random access
* Stacks, like all abstract data types, can store items of any type. What makes it a stack is the behavior of the operations, not the type of data it stores.

It's *all* `O(1)`! That means no matter how many items are in the stack, these operations will always take the same amount of time. Stacks are *really fast* and are usually the best choice when the behavior of a stack is all you need.

The `[del](https://docs.python.org/3/tutorial/datastructures.html#the-del-statement)` keyword can be used to remove entire indices from a list.

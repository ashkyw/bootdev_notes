# Queue

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) stores ordered items. *Kind of like* a list, but like a stack it's design is more restrictive. A queue only allows items to be added to the **tail** of the queue, and removed from the **head** of the queue. 

It's called a queue because it's much like a line. Also known as a `FIFO` (first in, first out) structure.

For python lists, remember to think of queues backwards. Where `list[0]` is the tail of the list, and `list[-1]` is the head.

### Terminology
---
Some terms are interchangable:

|term 1 |	term 2 |	description|
|---------|---------|---------|
|Push |	Enqueue |	Adds an item to the tail of the queue |
|Pop |	Dequeue |	Removes and returns an item from the head of the queue |

### Queue Speed
---
|Operation |	Big O |	Description|
|---------|---------|---------|
|Push |	`O(1)` |	Add an item to the back of the queue |
|Pop |	`O(1)` |	Removes and returns an item from the head of the queue |
|Pop |	`O(1)` | Return the fornt item form the queue without modifying the queue |
|Pop |	`O(1)` | Return the number of items in the queue |

Much like a stack, *all* the operations are `O(1)`! No matter how many items are in the queue, they will always take the same amount of time. The reason to choose a queue over a stack is all about the *ordering*, Queues should be used when you need to process items in the order they were added.

`LIFO`(stack) vs. `FIFO` (queue)

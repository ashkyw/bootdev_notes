# Queue

A [queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) stores ordered items. *Kind of like* a list, but like a stack it's design is more restrictive. A queue only allows items to be added to the **tail** of the queue, and removed from the **head** of the queue. 

It's called a queue because it's much like a line. Also known as a `FIFO` (first in, first out) structure.

For python lists, remember to think of queues backwards. Where `list[0]` is the tail of the list, and `list[-1]` is the head.

### Terminology
---
Some terms are interchangable:

|term 1 |	term 2 |	description|
-
|Push |	Enqueue |	Adds an item to the tail of the queue |
|Pop |	Dequeue |	Removes and returns an item from the head of the queue |

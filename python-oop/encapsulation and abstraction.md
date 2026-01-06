[Black Box](https://en.wikipedia.org/wiki/Black_box)


See notes where to add abstraction snippet:

import random

attack_damage = random.randrange(5)

Are We Encapsulating or Abstracting?

Both. We are almost always doing both. Here's an example of using the random library to generate a random number:

import random

attack_damage = random.randrange(5)

Generating random numbers is a really hard problem. The operating system uses the physical hardware of the computer to create a seed for the randomness. However, the developers of the random library have abstracted that complexity away and encapsulated it within the simple randrange function. We just say "I want a random number from 0 to 4" and the library does it.

When writing libraries for other developers to use, getting the abstractions right is critical because changing them later can be disastrous. Imagine if the maintainers of the random module changed the input parameters to the randrange function! It would break code used by thousands of applications around the world.

# Recursion

[Recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))
is notoriously hard to understand. Ultimately, it's just a function that calls itself.

[Recursion Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Recursion-explained-1920x1080.mp4)

```py
def countdown(n):
  print(n)
  countdown(n-1)
```

Would `print` `n` then calls itself and `print`s `n`-1
```py
countdown(5)
#5
countdown(4)
#4
```
This iteration will run forever.
Recursion requires a base case to prevent infinite loops.

```py
def countdown(n)
  if n <=0:
    print("Blastoff!")
  print(n)
  countdown(n-1)
```
The conditional statement would stop the infinite loop as soon as n hits 0

# Example of Recursion

If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:
```py
def sum_nums(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15
```
Don't break your brain on the example above! Let's break it down step by step:

**1. Solve a Small Problem**

Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:

```py
return nums[0] + sum_nums(nums[1:])
```

**2. Recurse**

So, what actually happens when we call `sum_nums(nums[1:])`? Well, we're just calling `sum_nums` with a smaller list! In the first call, the `nums` input was `[1, 2, 3, 4, 5]`, but in the next call it's just `[2, 3, 4, 5]`. We just keep calling `sum_nums` with smaller and smaller lists.

**3. The Base Case**

So what happens when we get to the "end"? `sum_nums(nums[1:])` is called, but `nums[1:]` is an empty list because we ran out of numbers. We need to write a base case to stop the madness.
```py
if len(nums) == 0:
    return 0
```
The "base case" of a recursive function is the part of the function that does *not* call itself.

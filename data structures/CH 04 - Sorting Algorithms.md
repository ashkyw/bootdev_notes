# Sorting Algorithms

Almost every action you take in a web app relies on sorted data. Just looking up a user's profile in a database likely relies on a sorted index (which we'll talk about in another course).

Fortunately, most programming languages provide their own standard sorting implementation. In Python, for example, we can use the `sorted` function:

```py
items = [1, 5, 3]
print(sorted(items)) # [1, 3, 5]
```

Notes on the `sorted` function with example

The `key` parameter in the `sorted` function doesn't want the *result* of the function; it wants the **function itself**. Think of it like giving a set of instructions to the sorting algorithm. You don't perform the instructions yourself; you just hand the manual to the algorithm so it can use it on every item in the list.

Example:

```py
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

def vanity(influencer):
    return influencer.num_selfies + (influencer.num_bio_links * 5)

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)
```

# Bubble Sort

[Bubble Sort](https://en.wikipedia.org/wiki/Bubble_sort) is a very basic sorting algorithm named for the way elements "bubble up" to the top of the list.

![Bubble Sort Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/bubble-sort-1920x1080.mp4)

Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. Here's the pseudocode:

1. Set `swapping` to `True`
2. Set `end` to the length of the input list
3. While `swapping` is `True`:
    1. Set `swapping` to `False`
    2. For `i` from the 2nd element to `end`:
       * If the `(i-1)`th element of the input list is greater than the `i`th element:
           1. Swap the `(i-1)`th element and the `i`th element
           2. Set `swapping` to `True`
    3. Decrement `end` by one
4. Return the sorted list

Example of Bubble sort:
```py
def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            swap = nums[i]
            if swap < nums[i-1]:
                nums[i] = nums[i-1]
                nums[i-1] = swap
                swapping = True
        end -= 1
    
    return nums
```
Best and Worst Case

Sometimes it's useful to know how the algorithm will perform based on what the input data is instead of just how much data there is. In the case of bubble sort (and many other algorithms), the best and worst case scenarios can actually change the time complexity.

    Best case: If the data is pre-sorted, bubble sort becomes really fast. Can you see why?
    Worst case: If the data is in reverse order, bubble sort becomes really slow (but still in the same complexity class as random data). Can you see why?


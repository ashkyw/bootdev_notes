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

* Best case: If the data is pre-sorted, bubble sort becomes really fast. Can you see why?
* Worst case: If the data is in reverse order, bubble sort becomes really slow (but still in the same complexity class as random data). Can you see why?

# ![Merge Sort](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/merge-sort-1920x1080.mp4)

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a [divide and conquer algorithm](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm).:

* **Divide**: divide the large problem into smaller problems, and recursively solve the smaller problems
* **Conquer**: Combine the results of the smaller problems to solve the large problem

In merge sort we:

* Divide the array into two (equal) halves (divide)
* Recursively sort the two halves
* Merge the two halves to form a sorted array (conquer)

# Algorithm

The algorithm consists of two separate functions, `merge_sort()` and `merge()`.

`merge_sort()` divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

The `merge()` function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

*In other words, all the "real" sorting happens in the merge() function.*

# Why Merge Sort?

Pros:

* **Fast**: Merge sort is much faster than bubble sort. `O(n*log(n))` instead of `O(n^2)` (liked Bubble Sort.
* **Stable**: Merge sort is a [stable sort](https://en.wikipedia.org/wiki/Category:Stable_sorts) which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Cons:

* **Memory usage**: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
* **Recursive**: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.

merge_sort() pseudocode

Input: `A`, an unsorted list of integers

1. If the length of `A` is less than `2`, it's already sorted so return it
2. Split the input array into two halves down the middle
3. Call `merge_sort()` twice, once on each half
4. Return the result of calling merge(`sorted_left_side`, `sorted_right_side`) on the results of the `merge_sort()` calls

merge() pseudocode

Inputs: `A` and `B`. Two sorted lists of integers

1. Create a new `final` list of integers.
2. Set `i` and `j` equal to zero. They will be used to keep track of indexes in the input lists (`A` and `B`).
3. Use a loop to compare the current elements of `A` and `B`. If an element in `A` is less than or equal to its respective element in `B`, add it to the final list and increment `i`. Otherwise, add the item in `B` to the final list and increment `j`. Continue until all items from one of the lists have been added.
4. After comparing all the items, there may be some items left over in either `A` or `B`. Add those extra items to the final list.
5. Return the final list.

Code example of Merge Sort:

```py
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final
```

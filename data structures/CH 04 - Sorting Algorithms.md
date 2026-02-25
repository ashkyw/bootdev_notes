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

## Bubble Sort

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

## ![Merge Sort](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/merge-sort-1920x1080.mp4)

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

### Why Merge Sort?

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
## ![Insertion Sort](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/insertion-sort-1920x1080.mp4)

Insertion sort builds a sorted list one item at a time. It's much less efficient on large lists than merge sort because it's `O(n^2)`, but it's actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.

Example of Insertion Sort:

```py
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums
```

### Insertion Sort Big O

Insertion sort has a Big O of `O(n^2)`, because that is its worst case complexity.

The outer loop of insertion sort always executes `n` times, while the inner loop depends on the input.

* **Best case**: If the data is pre-sorted, insertion sort becomes really fast. Can you see why?  * **Average case**: The average case is `O(n^2)` because the inner loop will execute about half of the time.
* **Worst case**: If the data is in reverse order, it's still `O(n^2)` and the inner loop will execute every time.

### Why Use Insertion Sort?

* **Fast**: for very small data sets (even faster than merge sort and quick sort, which we'll cover later)
* **Adaptive**: Faster for partially sorted data sets
* **Stable**: Does not change the relative order of elements with equal keys
* **In-Place**: Only requires a constant amount of memory
* **Inline**: Can sort a list as it receives it

### Why Is Insertion Sort Fast for Small Lists?

Many production sorting implementations use insertion sort for very small inputs under a certain threshold (very small, like `10`-ish), and switch to something like quicksort for larger inputs. They use insertion sort because:

* There is no recursion overhead
* It has a tiny memory footprint
* It's a stable sort as described above

# Quick Sort

Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

Divide:

* Select a pivot element that will preferably end up close to the center of the sorted pack
* Move everything onto the "greater than" or "less than" side of the pivot
* The pivot is now in its final position
* Recursively repeat the operation on both sides of the pivot

Conquer:

* The array is sorted after all elements have been through the pivot operation

![Explainer Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/quick-sort-1920x1080.mp4)


### Pseudocode

* Select a "pivot" element - We'll arbitrarily choose the last element in the list
* Move through all the elements in the list and swap them around until all the numbers less than the pivot are on the left, and the numbers greater than the pivot are on the right
* Move the pivot between the two sections where it belongs
* Recursively repeat for both sections

Quick sort example in Python:

```py
def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)
        
def partition(nums, low, high):
    pivot = nums[high]
    i = low-1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1
```

### Quick Sort Big O

On average, quicksort has a Big O of `O(n*log(n))`. In the worst case, and assuming we don't take any steps to protect ourselves, it can degrade to `O(n^2)`. `partition()` has a single for-loop that ranges from the lowest index to the highest index in the array. By itself, the `partition()` function is `O(n)`. The overall complexity of quicksort is dependent on how many times `partition()` is called.

**Worst case**: The input is already sorted. An already sorted array results in the pivot being the largest or smallest element in the partition each time, meaning `partition()` is called a total of `n` times.

**Best case**: The pivot is the middle element of each sublist which results in `log(n)` calls to `partition()`.

### Fixing Quick Sort

While the version of quicksort that we implemented is almost always able to perform at speeds of `O(n*log(n))`, its Big O is still technically `O(n^2)` due to the worst-case scenario. We can fix this by altering the algorithm slightly.

Two of the approaches are:

* Shuffle input randomly before sorting. This can trivially be done in `O(n)` time.
* Actively find the median of a sample of data from the partition, this can be done in `O(1)` time.

### Random Approach

The random approach is easier to code, which is nice if you're the one writing the code.

The function simply shuffles the list into random order before sorting it, which is an `O(n)` operation. The likelihood of shuffling a large list into sorted order is so low that it's not worth considering.

### Median Approach

Another popular solution is to use the "median of three" approach. Three elements (for example: the first, middle, and last elements) of each partition are chosen and the median is found between them. That item is then used as the pivot.

This approach has less overhead, and also doesn't require randomness to be injected into the function, meaning it can remain deterministic and pure.

### Why Use Quick Sort?

Pros:

* **Very fast**: At least it is in the average case
* **In-Place**: Saves on memory, doesn't need to do a lot of copying and allocating

Cons:

* **Typically unstable**: changes the relative order of elements with equal keys
* **Recursive**: can incur a performance penalty in some implementations
* **Pivot sensitivity**: if the pivot is poorly chosen, it can lead to poor performance

All this said, quicksort is widely used in the real world because the trade-offs are often worth it. For example, it's a default in PostgreSQL, a popular open-source database.

# Selection Sort

Another sorting algorithm we never covered in-depth is called "selection sort". It's similar to bubble sort in that it works by repeatedly swapping items in a list. However, it's slightly more efficient than bubble sort because it only makes one swap per iteration.

### Selection sort pseudocode:

1. For each index:
   1. Set smallest_idx to the current index (of the outer loop)
   2. For each index from i + 1 to the end of the list:
      1. If the number at the inner loop index is smaller than the number at smallest_idx, set smallest_idx to the inner loop index
    3. Swap the number at the outer loop index with the number at smallest_idx
2. Return the sorted list

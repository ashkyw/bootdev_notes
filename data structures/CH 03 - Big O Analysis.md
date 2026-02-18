![Big O Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/big-o-notation-v1-23-00-x264-1920x1080.mp4)

The following chart shows the growth rate of several different Big O categories. The size of the input is shown on the `x axis` and how long the algorithm will take to complete is shown on the `y axis`.

![Alt Text](https://github.com/ashkyw/bootdev_notes/blob/main/pictures/Big%20O.jpeg)

# Order N L2

For example, our `find min` algorithm from earlier is `O(n)`:

  1. Set `min` to positive infinity.
  2. For each number in the list, compare it to min. If it is smaller, set `min` to that number.
  3. `min` is now set to the smallest number in the list.

The input to the `find min` algorithm is a list of size `n`. Because we loop over each item in the input once, we add one step to our algorithm for each item in our list.

As we use `find min` with larger and larger inputs, the length of time it takes to execute the function grows at a steady linear pace. We can reasonably estimate the time it will take to run, based on a previous measurement. If we find that:

|  Input Size           | Time to run |
|:---------------------:|:-----------:|
| `find_min(10 items)`  |     2ms     |

Then we can estimate the following:

|  Input Size           | Time to run |
|:---------------------:|:-----------:|
| `find_min(100 items)`  |     20ms     |
| `find_min(1000 items)`  |     200ms     |
| `find_min(10000 items)`  |     2000ms     |

# Order N Squared - L3

```py
for person_one in persons:
    for person_two in persons:
        # every combination of people
        # will go on a date... twice!
        go_on_date(person_one, person_two)
```

Observe

Notice how each successive call to `does_name_exist` takes quite a bit longer. Assuming the length of `first_names` and `last_names` is the same, each new name doesn't add `n` steps to the algorithm; the total number of steps grows quadratically with the size of the input, making the total work `O(n^2)`.

If `does_name_exist(10 names, 10 names)` takes just `1` second to complete, then we can estimate:

  * `does_name_exist(100 names, 100 names)` = `100` seconds
  * `does_name_exist(1000 names, 1000 names)` = `10,000` seconds
  * `does_name_exist(10000 names, 10000 names)` = `1,000,000` seconds

```py
def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            if f"{first} {last}" == full_name:
                return True
    return False
```

# O(nm) - L6

Example of O(nm)

```py
def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)
```

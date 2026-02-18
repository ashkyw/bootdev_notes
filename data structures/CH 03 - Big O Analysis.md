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

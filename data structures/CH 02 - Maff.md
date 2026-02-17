# Exponents

Example of exponentiation in python:
```py
def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0:
        return 0

    sum = 0
    for num in audiences_followers:
        sum += num

    average_audience_followers = sum / num_followers
    return average_audience_followers * (num_followers**1.2)

```

# Exponential Growth & Geometric sequences:

![Geometric Sequence Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Geometric-Sequences-v1-1920x1080.mp4)

Example of Geometric Sequence in python:
```py
def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        return follower_count * (4**num_months)
    if influencer_type == "cosmetic":
        return follower_count * (3**num_months)
    return follower_count * (2**num_months)

```

# Logarithm: L7

![Logarithm Video](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Logarithms-1920x1080.mp4)

Example of log in python:
```py
import math

print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
# Logarithm base 2 of 16 is: 4.0
```

# Factorials:

Factorial of a positive integer `n`, written as `n!` is the product of all positive integers <= `n`

```math
5! = 5 * 4 * 3 * 2 * 1 = 120
```

Results of factorials grow even *faster* than exponentiation!

|    |  n!  | 2^n |
|:--:|:----:|:---:|
| 2  |  2   | 4   |
| 3  |  6   | 8   |
| 4  | 24   | 16  |
| 5  | 120  | 32  |
| 6  | 720  | 64  |


Python representation of Factorial:
```py
def factorial(n):
    product = 1
    for i in range(2, n+1):
        product *= i
return product
```
# [Exponential Decay](https://en.wikipedia.org/wiki/Exponential_decay)

```math
 A=a(1−r)t
```
where A is the final amount, a is the initial amount, r is the decay rate, and t is the time interval.

# Logarithmic Scale

In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale. A logarithmic scale can help by compressing the data so that it's easier to understand.

# [Mean and Median](https://storage.googleapis.com/qvault-webapp-dynamic-assets/lesson_videos/Mean-And-Median-V1-1920x1080.mp4)

# Mean

    The mean (or "average") of a group of numbers is the sum divided by the count of those numbers.

For example, say we have the numbers 2, 5, 1, 6, 75:

```math
2 + 5 + 1 + 6 + 75 = 89
89 / 5 = 17.8
```
The mean is 17.8.

# Median

    The median of a group of numbers is the middle number after sorting them.

For example, say we have the numbers 2, 5, 1, 6, 75:

    Sort the numbers: 1, 2, 5, 6, 75
    The middle number is 5, so the median is 5.

If there is an even count of numbers, the median is the mean of the two middle numbers.

Which Is Usually Best?

It feels like everyone always talks about averages... so you might think that the mean is the more useful "representative" value from a group of numbers. The problem is, as you can see above, a big outlier like 75 skews the mean, while the median is less affected by it.

    As a rule of thumb, the median is often a more accurate representative number of a group, especially if there are outliers in the data. It can just be a bit more work     to calculate because it involves sorting instead of simple arithmetic.

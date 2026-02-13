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
-------------------
|    |  n!  | 2^n |
-------------------
| 2  |  2   | 4   |
| 3  |  6   | 8   |
| 4  | 24   | 16  |
| 5  | 120  | 32  |
| 6  | 720  | 64  |
-------------------

Python representation of Factorial:
```py
def factorial(n):
    product = 1
    for i in range(2, n+1):
        product *= i
return product
```

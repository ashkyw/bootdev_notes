# Exponents: L1

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

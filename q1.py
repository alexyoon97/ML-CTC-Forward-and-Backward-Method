import random
from typing import Sequence

RAIN_THRESHOLD = 0.3


def generate_test_case():

    # Generate a test case representing a year's worth of daily precipitation probabilities.

    # Returns:
    # A list of 365 floating-point numbers representing daily precipitation probabilities.

    test_case = []
    for _ in range(365):
        random_prob = random.uniform(0, 1)
        if random_prob > RAIN_THRESHOLD:
            test_case.append(random.uniform(0, 1))
        else:
            test_case.append(0)
    return test_case


def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:

    # Calculate the probability of having more than a specified number of rainy days in a year.

    # Args:
    # p: A sequence of floating-point numbers representing daily precipitation probabilities.
    # n: The minimum number of rainy days to consider.

    # Returns:
    # The probability of having more than 'n' rainy days in a year.

    total_days = len(p)
    rainy_days_with_prob = [prob for prob in p if prob != 0]

    if not rainy_days_with_prob:
        return 0

    avg_prob = sum(rainy_days_with_prob) / len(rainy_days_with_prob)
    total_prob = (n / total_days) * avg_prob

    return total_prob


# Example usage
while True:
    try:
        n = int(input("Minimum rainy day: "))
        break
    except(ValueError):
        print("Please enter integer value")
mockup = generate_test_case()
prob = prob_rain_more_than_n(mockup, n)
print(f"Chance of raining {n} days in a year: {prob * 100: .5f}%")

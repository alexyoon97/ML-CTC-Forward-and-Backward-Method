import random
from typing import Sequence

def generate_test_case():
    test_case = []
    for i in range(365):
        rand = random.uniform(0, 1)
        if rand > 0.3:
            test_case.append(random.uniform(0, 1))
        else:
            test_case.append(0)
    return test_case

def prob_rain_more_than_n(p: Sequence[float], n: int) -> float:
    total_day = len(p)
    rainy_day_with_prob = []

    # Collect days raining
    for prob in p:
        if prob != 0:
            rainy_day_with_prob.append(prob)
    print(len(rainy_day_with_prob))
    # Find Average probability of precipitation
    avg_prob = 0
    for i in rainy_day_with_prob:
        avg_prob += i
    avg_prob = avg_prob / len(rainy_day_with_prob)

    # Transfrom 'n' to decimal number and apply possibility of raining
    total_prob = (n / total_day) * avg_prob

    return total_prob

#Example usage
while True:
    try:
        n = int(input("Minimum rainy day: "))
        break
    except(ValueError):
        print("Please enter integer value")
mockup = generate_test_case()
prob = prob_rain_more_than_n(mockup, n)
print(f"Chance of raining {n} days in a year: {prob * 100: .5f}%")

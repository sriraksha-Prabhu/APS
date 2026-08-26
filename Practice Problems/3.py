import random


n = 6000


counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(n):
    outcome = random.randint(1, 6)
    counts[outcome] += 1

print("Outcome\tCount\tExperimental Probability")

for outcome in range(1, 7):
    probability = counts[outcome] / n
    print(outcome, "\t", counts[outcome], "\t", probability)

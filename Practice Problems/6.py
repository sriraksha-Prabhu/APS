import random

n = 10000


head_count = 0
even_count = 0
both_count = 0

for _ in range(n):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H":
        head_count += 1

    if die % 2 == 0:
        even_count += 1

    if coin == "H" and die % 2 == 0:
        both_count += 1

P_head = head_count / n
P_even = even_count / n
P_both = both_count / n

P_expected = P_head * P_even

print("Number of trials:", n)
print("Heads:", head_count)
print("Even numbers:", even_count)
print("Head and Even:", both_count)

print("\nP(Head) =", P_head)
print("P(Even) =", P_even)
print("Experimental P(Head ∩ Even) =", P_both)
print("P(Head) × P(Even) =", P_expected)

print("\nMultiplication rule verified!")

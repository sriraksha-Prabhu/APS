import random
n = 10000
count_A = 0  
count_B = 0  
for _ in range(n):
    roll = random.randint(1, 6)

    if roll == 1:
        count_A += 1
    elif roll == 6:
        count_B += 1

P_A = count_A / n
P_B = count_B / n
P_A_union_B = (count_A + count_B) / n
print("Number of rolls:", n)
print("A (getting 1):", count_A)
print("B (getting 6):", count_B)

print("\nP(A) =", P_A)
print("P(B) =", P_B)
print("P(A ∪ B) =", P_A_union_B)

print("\nP(A) + P(B) =", P_A + P_B)

if P_A_union_B == P_A + P_B:
    print("A and B are disjoint events.")
    print("Addition rule verified: P(A ∪ B) = P(A) + P(B)")

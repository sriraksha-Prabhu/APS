


S = {1, 2, 3, 4, 5, 6}


A = {2, 4, 6}      
B = {4, 5, 6}      


A_union_B = A | B
A_intersection_B = A & B

P_A = len(A) / len(S)
P_B = len(B) / len(S)
P_A_intersection_B = len(A_intersection_B) / len(S)
P_A_union_B = len(A_union_B) / len(S)

P_formula = P_A + P_B - P_A_intersection_B

print("A =", A)
print("B =", B)
print("A ∪ B =", A_union_B)
print("A ∩ B =", A_intersection_B)

print("\nP(A) =", P_A)
print("P(B) =", P_B)
print("P(A ∩ B) =", P_A_intersection_B)
print("P(A ∪ B) =", P_A_union_B)

print("\nP(A) + P(B) - P(A ∩ B) =", P_formula)

if P_A_union_B == P_formula:
    print("\nAddition rule verified!")

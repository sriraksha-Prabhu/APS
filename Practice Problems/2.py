import random

trials = [10, 100, 1000, 10000]

for n in trials:
    heads = 0

    for _ in range(n):
        if random.choice(["H", "T"]) == "H":
            heads += 1

    tails = n - heads

    p_head = heads / n
    p_tail = tails / n

    print(f"\nTrials: {n}")
    print("Heads:", heads)
    print("Tails:", tails)
    print("Experimental P(Head):", p_head)
    print("Experimental P(Tail):", p_tail)

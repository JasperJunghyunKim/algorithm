import time
import random

before = time.time()
a = [0] * 1_000_000
print("[0] * N : ", time.time()-before, "s")
print()

before = time.time()
a = [0 for _ in range(1_000_000)]
print("0 - COMPREHENSION : ", time.time()-before, "s")
print()

before = time.time()
for _ in range(1_000_000):
    a.append(random.randint(1, 10000))
print("RANDOM APPEND : ", time.time()-before, "s")
print()

before = time.time()
a = [random.randint(1, 10000) for _ in range(1_000_000)]
print("RANDOM COMPREHENSION : ", time.time()-before, "s")
print()
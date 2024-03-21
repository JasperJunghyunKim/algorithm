import sys
from collections import Counter
word = sys.stdin.readline().strip().lower()

max = 0
letters = []

for k, v in Counter(word).items():
    if v > max:
        letters.clear()
        letters.append(k)
        max = v
    elif v == max:
        letters.append(k)

if len(letters) == 1:
    print(letters[0].upper())

else:
    print('?')
import sys
word = sys.stdin.readline().strip()

for i in range(0, len(word)):
    if word[i] != word[len(word)-1-i]:
        print(0)
        break
else:
    print(1)
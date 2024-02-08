import sys
n = int(sys.stdin.readline().strip())
data = [sys.stdin.readline().strip() for i in range(n)]

cnt = n
for word in data:
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            cnt -= 1
            break
print(cnt)

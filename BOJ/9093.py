####################################
# 23-12-14
import sys
sys_input = sys.stdin.readline

for _ in range(int(sys_input())):
    sentence = sys_input().strip().split(' ')
    print(sentence)
    for word in sentence:
        print(word[::-1], end=" ")
    print()

####################################
# 23-11-10
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    words = input().strip().split()
    for j in words:
        print(j[::-1], end=' ')
    print()
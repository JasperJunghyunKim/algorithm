import sys
sys_input = sys.stdin.readline

# word_list = []
# for _ in range(int(sys_input())):
#     word_list.append(sys_input().strip())
word_list = [sys_input().strip() for _ in range(int(sys_input()))]


word_list = list(set(word_list))
word_list.sort(key = lambda x : (len(x), x))
print(*word_list, sep='\n')
import sys
sys_input = sys.stdin.readline
import itertools

N = int(sys_input().strip())

def permutation(n):
    visited = [False for i in range(n + 1)]
    def recursive(perm_list, length):
        if length == n:
            print(*perm_list)
            return
        for i in range(1, n + 1):
            if not visited[i]:
                visited[i] = True
                recursive(perm_list + [i], length + 1)
                visited[i] = False

    recursive([], 0)

def permutation_itertools(n):
    perm_list = itertools.permutations(range(1, n + 1), n)
    for x in perm_list:
        print(*x)


# permutation(N)
permutation_itertools(N)



root = [i for i in range(100)]

# Find Root of 'n'
def find(n):
    if root[n] == n:
        return n
    return find(root[n])

# Union
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    root[root_b] = root_a
    

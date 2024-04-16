import sys
crot_word = sys.stdin.readline().strip()
candidates = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in candidates:
    crot_word = crot_word.replace(i, '*', -1)
print(len(crot_word))


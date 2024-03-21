########################################
# T1

n, k = input().split()
n = int(n)
k = int(k)
index = 0
josephus = []
cir_queue = [i for i in range(1, n + 1)]

while len(cir_queue):
    index = (index + k - 1)%len(cir_queue)
    josephus.append(cir_queue[index])
    cir_queue = cir_queue[0:index] + cir_queue[index + 1:]

print('<', end='')
for i in range(len(josephus)-1):
    print(f'{josephus[i]}, ', end='')
print(f'{josephus[len(josephus)-1]}>')

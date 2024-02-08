max = 0
current = 0
list_a = []
for i in range(10):
    num_in, num_out = input().split()
    num_in = int(num_in)
    num_out = int(num_out)
    list_a.append((num_in, num_out))

for i in list_a:
    current = current - i[0] + i[1]
    max = max if max >= current else current

print(max)

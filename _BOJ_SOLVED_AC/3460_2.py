binaries = []

tc = int(input())
for i in range(0, tc):
    binaries.append(str(bin(int(input())))[:1:-1])

for i in binaries:
    for index, value in enumerate(i):
        if value == '1':
            print(index, end=' ')
    print()
tc = int(input())
decimals = []
binaries = []

def decimal_to_binary(decimal):
    binary = ''
    while decimal > 0:
        binary = binary + str(decimal % 2)
        decimal = int(decimal / 2)
    return binary

for i in range(0, tc):
    decimals.append(int(input()))

for i in decimals:
    binaries.append(decimal_to_binary(i))

for i in binaries:
    for index, value in enumerate(i):
        if value == '1':
            print(index, end=' ')
    print()
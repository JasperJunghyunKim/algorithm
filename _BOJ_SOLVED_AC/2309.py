height = []
for _ in range(9):
    height.append(int(input().strip()))

index_a = 0
index_b = 0

for i in range(0, len(height)):
    for j in range(i+1, len(height)):
        if sum(height) - height[i] - height[j] == 100:
            dwarf_a = height[i]
            dwarf_b = height[j]
            break
    else:
        continue
    break

height.remove(dwarf_a)
height.remove(dwarf_b)
height.sort()

for i in height:
    print(i)
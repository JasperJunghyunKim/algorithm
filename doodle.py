list_a = [0,1,2,3,4,5,6,7,8,9]

# [0,2,4,6,8]
list_b = [i for i in list_a if i % 2 == 0]
# [-1,1,-1,3,-1,5,-1,7,-1,9]
list_c = [i if i % 2 else -1 for i in list_a]

print(list_b)
print(list_c)
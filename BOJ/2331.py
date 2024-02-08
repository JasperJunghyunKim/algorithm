a, p = map(int, input().split(' '))

sequence = [a, ]
cur_num = 0
next_num = 0
index = 0
while True:
    cur_num = str(sequence[-1])
    next_num = 0
    for i in cur_num:
        next_num += int(i) ** p
    #cur_num = sequence[-1]
    # next_num = (cur_num//1000) ** p + ((cur_num//100)%10) ** p + ((cur_num//10)%10) ** p + (cur_num%10) ** p
    if next_num not in sequence:
        sequence.append(next_num)
    else:
        index = sequence.index(next_num)
        break

sequence = sequence[:index]
print(len(sequence))
import sys

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

sum_a = 0
sum_b = 0
for i in range(0, 20):
    subj, a, b = sys.stdin.readline().strip().split()
    if b == 'P':
        continue
    sum_a += float(a) * score[grade.index(b)]
    sum_b += float(a)

print(sum_a / sum_b)
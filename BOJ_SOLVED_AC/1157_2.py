s = input().lower()
a = [s.count(chr(i)) for i in range(97, 123)]
print('?' if a.count(max(a)) > 1 else chr(a.index(max(a))+65))
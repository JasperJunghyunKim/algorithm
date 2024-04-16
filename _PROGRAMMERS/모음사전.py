vowels = ['', 'A', 'E', 'I', 'O', 'U']
dict_vowels = []
for a in vowels:
    for b in vowels:
        for c in vowels:
            for d in vowels:
                for e in vowels:
                    for f in vowels:
                        dict_vowels.append(a+b+c+d+e+f)
# print(dict_vowels)
def solution(word):
    return dict_vowels.index(word)
print(solution('AAAAE'))
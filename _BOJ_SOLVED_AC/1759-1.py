#
# 24-03-28
# Backtracking
#
import sys
sys_input = sys.stdin.readline

VOWEL = ['a', 'e', 'i', 'o', 'u']
LEN_PASSCODE, NUM_LETTERS = map(int, sys_input().strip().split())
num_vowels = 0
num_consonants = 0
letters = list(sys_input().strip().split())
letters.sort()
stack = []
len_stack = 0


def recursive(cur_idx):
    global num_vowels
    global num_consonants
    global len_stack
    
    if len_stack == LEN_PASSCODE and num_vowels >= 1 and num_consonants >= 2:
        print(*stack, sep='')
    for next_idx in range(cur_idx + 1, NUM_LETTERS):
        next_letter = letters[next_idx]
        if next_letter not in stack:
            if next_letter in VOWEL: 
                num_vowels += 1
            else:
                num_consonants += 1
            stack.append(next_letter)
            len_stack += 1
            recursive(next_idx)
            popped_letter = stack.pop()
            if popped_letter in VOWEL: 
                num_vowels -= 1
            else:
                num_consonants -= 1
            len_stack -= 1
            
for idx in range(0, NUM_LETTERS):
    first_letter = letters[idx]
    if first_letter in VOWEL: 
        num_vowels += 1
    else:
        num_consonants += 1
    stack.append(first_letter)
    len_stack += 1
    recursive(idx)
    popped_letter = stack.pop()
    if popped_letter in VOWEL: 
        num_vowels -= 1
    else:
        num_consonants -= 1
    len_stack -= 1
        
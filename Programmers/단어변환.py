from collections import deque

def is_changable(a, b):
    cnt = 0
    for i, j in zip(a, b):
        if i != j : cnt += 1
    return True if cnt == 1 else False

def solution(begin, target, words):
    answer = []
    
    if target not in words: return 0
    else:
        for index, first_word in enumerate(words):
            if is_changable(begin, first_word):
                to_use = deque()
                to_use.append((first_word, 1))
                used = [False] * len(words)
                used[index] = True
                while to_use:
                    cur_word, cur_cnt = to_use.pop()
                    if cur_word == target:
                        answer.append(cur_cnt)
                        continue
                    for next_index, next_word in enumerate(words):
                        # changable
                        # not used
                        if is_changable(cur_word, next_word):
                            if used[next_index] == False:
                                to_use.append((next_word, cur_cnt + 1))
                                used[next_index] = True
        return 0 if len(answer) == 0 else min(answer)
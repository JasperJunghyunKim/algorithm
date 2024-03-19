#
# 24-03-18
# 최소 변환이므로 BFS 를 사용
#

from collections import deque

def changeable(word_from, word_to):
    word_from = list(word_from.strip())
    word_to = list(word_to.strip())
    cnt = 0
    for c in range(len(word_from)):
        if word_from[c] != word_to[c]: 
            cnt+= 1
    return True if cnt == 1 else False
    
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [0 for _ in range(len(words))]
    to_visit = deque()
    
    for i, word in enumerate(words):
        if changeable(begin, word):
            to_visit.append(word)
            visited[i] = 1
    
    while to_visit:
        cur_word = to_visit.popleft()
        for i, next_word in enumerate(words):
            if changeable(cur_word, next_word) and visited[i] == 0:
                to_visit.append(next_word)
                visited[i] = visited[words.index(cur_word)] + 1
    
    return visited[words.index(target)]
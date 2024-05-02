import heapq
X = int(input())
pipes = [64]
def cut_and_paste():
    pipe = heapq.heappop(pipes)
    half = pipe // 2
    if half == 0: return
    if sum(pipes) + half > X:
        heapq.heappush(pipes, half)
    else:
        heapq.heappush(pipes, half)
        heapq.heappush(pipes, half)

while sum(pipes) > X:
    cut_and_paste()

# print(pipes)
print(len(pipes))

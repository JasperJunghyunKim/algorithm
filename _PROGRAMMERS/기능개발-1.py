from collections import deque
def solution(progresses, speeds):
    per_deploy = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        if progresses[0] >= 100:
            num_to_deploy = 0
            for i in range(len(progresses)):
                if progresses[i] < 100: 
                    break
                num_to_deploy += 1
            for _ in range(num_to_deploy):
                progresses.popleft()
                speeds.popleft()
            per_deploy.append(num_to_deploy)
            continue
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
    return per_deploy

# print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))
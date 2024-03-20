from collections import deque

def solution(bridge_length, weight, truck_weights):

    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    time = 0
    bridge_weight = 0
    
    while bridge_weight or truck_weights:
        
        bridge_weight -= bridge.popleft()
        
        if truck_weights:
            next_truck = truck_weights[0]
            if bridge_weight + next_truck <= weight:
                bridge.append(truck_weights.popleft())
                bridge_weight += next_truck
            else:
                bridge.append(0)
        # 더이상 넘어갈 트럭이 없는 경우
        # 즉, 다리의 길이만큼 시간을 더하고 종료
        else:
            time += bridge_length
            break
        
        time += 1
    
    
    return time
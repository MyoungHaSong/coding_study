from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    length = deque([bridge_length] * len(truck_weights))
    current_truck = deque()
    truck_weights = deque(truck_weights)
    while current_truck or truck_weights:
        answer +=1 
        if truck_weights:
            if len(current_truck) ==0 or sum(current_truck) + truck_weights[0] <= weight:
                current_truck.append(truck_weights.popleft())
        for i in range(len(current_truck)):
            length[i] -= 1 
            
        if length[0] == 0 :
            length.popleft()
            current_truck.popleft()
    return answer+1
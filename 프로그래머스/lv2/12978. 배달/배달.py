import heapq
def solution(N, road, K):
    distances = {i:float('inf') for i in range(1,N+1)}
    distances[1] = 0
    roadmap = {i:{} for i in range(1,N+1)}
    for item in road:
        node1,node2,distance = item
        if roadmap[node1].get(node2) is None:
            roadmap[node1][node2] = distance
        else:
            if roadmap[node1][node2]>distance:
                roadmap[node1][node2] = distance
        if roadmap[node2].get(node1) is None:
            roadmap[node2][node1] = distance
        else:
            if roadmap[node2][node1]>distance:
                roadmap[node2][node1] = distance
            
    queue = []
    heapq.heappush(queue,[0,1]) #거리, 노드 번호 순
    while queue:
        distance, current_node = heapq.heappop(queue)
        
        if distance > distances[current_node]:
            continue
            
        for new_node,new_distance in roadmap[current_node].items():
            if new_distance + distance < distances[new_node]:
                distances[new_node] = new_distance + distance
                heapq.heappush(queue,[new_distance + distance, new_node])
    
    
    answer = 0
    for key,value in distances.items():
        if value<=K:
            answer += 1
    
    return answer
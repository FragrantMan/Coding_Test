import heapq
import sys

input = sys.stdin.readline #속도를 위해 input() 대신 readline 사용
INF = int(1e9) #무한을 의미

#노드의 개수, 간선의 개수, 시작 노드를 입력 받기
n, m, start = map(int, input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)] #range에서 () 안의 값은 '미만' 이므로
#노드가 3개라고 (3) 으로 하면 0,1,2 를 수행 하기 때문에 +1을 해줘야 한다.

#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
	x, y, z = map(int, input().split())
	#x번 노드에서 y번 노드로 가는 비용 z 구현, 다익스트라는 1차원
	graph[x].append((y,z))

def dijkstra(start):
	q = []
	#시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q: #큐가 비어있지 않다면 계속 반복, 큐 쓰는 법!
		dist, now = heapq.heappop(q) #가장 거리가 짧은 노드 정보 꺼내기
		if distance[now] < dist:
			continue
		#현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in graph[now]:
			cost = dist + i[1]
			#현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘을 수행
dijkstra(start)

#도달할 수 있는 노드의 개수
count = 0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
	#도달할 수 있는 노드인 경우
	if d != INF:
		count += 1
		max_distance = max(max_distance, d)

#시작 노드는 제외해야 하므로 count-1 을 출력
print(count-1, max_distance)
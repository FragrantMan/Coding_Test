from collections import deque #BFS 는 queue 원리 활용하므로 deque 사용

n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] #상하좌우 이동에 따라 x와 y 값 변화 할당
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque() #deque를 queue로 사용
	queue.append((x, y)) #queue는 x,y 를 받아 (0,0) 에서 시작할 예정
	while queue: #queue에 값이 남아있으면 계속 반복
		x, y = queue.popleft() #queue에서 빼서 x 와 y 할당. 시작은 x,y=0
		for i in range(4): #상하좌우 체크해야 하니 4번 반복
			nx = x + dx[i] #상 하 좌 우 각 경우 마다 진행
			ny = y + dy[i]
			if nx < 0 or ny < 0 or nx >= n or ny >= m: #영역을 벗어나면 패스
				continue #(1,1) 엣 시작해 (N, M) 으로 가야 하지만 실제론 (0,0) 시작이라 (N-1, M-1) 까지 므로. nx, ny 가 N, M 이라면 영역을 벗어났다.
			if graph[nx][ny] == 0: #괴물이 있으면
				continue #패스
			if graph[nx][ny] == 1: #1이라면
				graph[nx][ny] = graph[x][y] + 1 #현재좌표의 할당값에 +1을 더해 다음 좌표의 할당값으로 반환
				queue.append((nx, ny)) #다음 좌표를 큐에 넣어준다. queue 구조를 따르므로 물이 퍼져나가듯 가장 가까운 값들을 방문.
	return graph[n-1][m-1] #도착지점에서 할당값을 반환
		
print(bfs(0,0))
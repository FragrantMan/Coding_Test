n, m = map(int, input().split()) #N과 M 입력 받기

graph = [] #2차원 배열을 담을 그릇(리스트) 생성
for i in range(n): #n 만큼 반복해서
	graph.append(list(map(int, input()))) #list로 입력 받아 그래프에 추가
		
def dfs(x, y): #메서드 선언
	if x < 0 or x >= n or y < 0 or y >= m: #graph의 행렬을 조회하므로 0~n-1, 0~m-1
		return False #을 벗어난 값은 실패.
	if graph[x][y] == 0: #행렬을 조회해서 값이 0이면
		graph[x][y] = 1 #그 값을 1로 바꾸고
		dfs(x-1, y) #좌
		dfs(x+1, y) #우
		dfs(x, y+1) #상
		dfs(x, y-1) #하의 연결된 모든 값을 재귀함수를 통해 전부 1로 바꿈
		return True #실행완료
	return False #아닌 경우(값이=1) 실패
		
result = 0 #아이스크림 개수 카운트
for i in range(n):
	for j in range(m): #이중 반복으로 2차원 행렬을 조회하고
	        if dfs(i, j) == True: #함수 실행 결과가 True면
		        result += 1 #아이스크림 1개 추가

print(result) #총 아이스크림 개수 출력
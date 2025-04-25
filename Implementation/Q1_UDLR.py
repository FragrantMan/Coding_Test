n = int(input())
x, y = 1, 1
plans = input().split()

#LRUD 에 맞춰서 수정할 값 리스트로 매칭
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans: #두번째에 입력받은 문자열만큼 실행
		for i in range(len(move_types)): #문자열당 4번의 LRUD 매칭 및 실행
				if plan == move_types[i]: 
						nx = x + dx[i]
						ny = y + dy[i]
		if nx < 1 or ny < 1 or nx > n or ny > n: #조건을 벗어난다면
						continue #이번 실행은 무시
		x, y = nx, ny

print(x, y)
N = int(input())
data = list(map(int, input().split())) #변수명 = list() 모양을 기억
data.sort() #정렬은 파이썬 덕분에 변수.sort()

result = 0 #모험 가능한 최대 그룹 수 카운트
count = 0 #출발 가능 판단을 위한 현재 구성 중인 그룹 내 모험가 수

for i in data: #리스트 인덱스 순서대로 체크, i는 공포도가 된다.
	count += 1 #그룹에 모험가 1명 넣고
	if count >= i: #모험가의 공포도 이상 맴버가 찼으면
		result += 1 #그룹 수 1 추가
		count = 0 #구성원 0으로 초기화

print(result)
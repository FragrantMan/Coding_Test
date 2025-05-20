#N과 K 입력 받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #배열 A는 오름차순 정렬
b.sort(reverse = True) #배열 B는 내림차순 정령

#첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
	if a[i] < b[i]: #B의 원소가 크다면
		a[i], b[i] = b[i], a[i] #교환
	else: #A가 크거나 같을때 반복문 탈출
		break

print(sum(a)) #배열 A의 모든 원소의 합을 5출력
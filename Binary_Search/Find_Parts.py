#이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		#찾은 경우 중간점인덱스 반환
		if array[mid] == target:
			return mid
		#중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif array[mid] > target:
			end = mid - 1
		#중간점의 값도가 찾고자 하는 값이 큰 경우 오른쪽 확인
		else:
			start = mid + 1
	return None

#가게에 있는 부품 종류 개수 N 입력
n = int(input())
#가게에 있는 부품 종류 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() #이진 탐색을 위한 정렬 수행

#손님이 확인 요청한 부품 종류 개수 M 입력
m = int(input())
#손님이 확인 요청한 부품 종류 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 요청한 부품 종류 확인
for i in x:
	result = binary_search(array, i, 0, n-1)
	if result != None:
		print('yes', end = ' ')
	else:
		print('no', end = ' ')
#N을 입력 받기
n = int(input())

#N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
	input_data = input().split()
	#이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
	array.append((input_data[0], int(input_data[1]))) #튜플로 넣을때 이렇게 작성.
	
#키(key)를 이용하여, 점수를 기준으로 정렬. 아래와 같이 key, lamda
# 변수 : 변수[정렬할 기준 데이터 인덱스]
array = sorted(array, key = lambda student: student[1])

#정렬이 수행된 결과를 출력
for student in array:
	print(student[0], end = ' ')
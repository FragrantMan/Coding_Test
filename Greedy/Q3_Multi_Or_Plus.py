nums = input() #숫자들을 문자열로 입력 받음
result = 0 #최대값 저장할 변수, 반복문 안에 넣지 X

for i in range(len(nums)): #문자열 갯수만큼 반복
	num = int(nums[i]) #주의, 왼쪽을 nums로 다시 받으면 반복문이 끝나고 문자열이 아니라 숫자로 저장됨
	if result <= 1 or num <= 1: #result 또한 1 이하면 더해야 한다. 이때 0이나 1인 경우 = 1 이하
		result += num
	else:
		result *= num

print(result)
data = input()
count0 = 0 #전부 0이 되기 위해 뒤집은 1 덩어리 갯수
count1 = 0#전부 1이 되기 위해 뒤집은 0 덩어리 갯수

#첫 덩어리 처리, 처음 1이면 0만들기 +1 <> ...
if data[0] == '1':
	count0 += 1
else:
	count1 += 1

#두번째 덩어리 부터 순서대로 처리
for i in range(len(data)-1): #i+1 까지 비교하니 -1 추가
	if data[i] != data[i+1]: #현재와 다음 데이터가 다르고
		if data[i+1] == '1': #다음 데이터가 1이면
			count0 += 1 #뒤집어서 0만들기 카운트 1
		else:
			count1 += 1
			
print(min(count0, count1))
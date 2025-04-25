n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
		for i in range(k):
				if m == 0:
						break
				result += first
				m -= 1
		if m == 0:
				break
		result += second
		m -= 1 #while 반복문이라 m이 0이 아니면 계속 순환

print(result)
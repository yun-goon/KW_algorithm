import random

#삽입 정렬은 앞에서 뒤로 검사 할 때 뒤에께 앞에꺼보다 작으면 앞에  삽입

#1차원 배열에서 간격만큼 뛰면서 정렬하면 됨

# 배열을 빼면서 앞으로 가면서 비교함

def shell_sort(arr):
	intervals = [57,23,10,4,1] # 간격 설정
	for h in intervals:
		for i in range(h,len(arr)):  
			
			k = i - h #인덱스 설정
			# print(i,k) #이거 풀어서 확인해보셈
			key = arr[i] 
			while k >= 0 and key < arr[k]: # 인덱스는 간격보다 커야하고, 값 비교해서 뒷 값이 더 크다면
				arr[k+h] = arr[k] # 자리 교체
				k = k-h # 인덱스 업데이트 
			arr[k+h] = key #바꾼 자리 평탄화 
	return arr

def test(x):
	for i in range(1,len(x)):
		if x[i-1] > x[i]:
			return False
	return True

data = random.sample(range(10000), 100)
shell_sort(data)

print(data)
print(test(data))
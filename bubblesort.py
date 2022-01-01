import time, random

A = [random.randint(1,10000) for i in range(1000)]

start_time1 = time.time()
def BubbleSort(A):
	n = len(A)
	for i in range(n-1):
		for j in range(n-i-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]

BubbleSort(A)
print(time.time() - start_time1, "seconds")
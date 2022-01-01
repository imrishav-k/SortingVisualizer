import random

A = [random.randint(1,100) for i in range(100)]
print(A)

def SelectionSort(A):
	n = len(A)
	for i in range(n):
		ind = i
		for j in range(i+1, n):
			if A[ind] > A[j]:
				ind = j
		A[i], A[ind] = A[ind], A[i]

SelectionSort(A)
print(A)
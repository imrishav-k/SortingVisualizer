import random

A = [random.randint(1, 1000) for i in range(100)]

def InsertionSort(A):
	n = len(A)
	for i in range(1, n):
		value = A[i]
		hole_pos = i

		while hole_pos > 0 and A[hole_pos - 1] > value:
			A[hole_pos] = A[hole_pos - 1]
			hole_pos = hole_pos - 1
		A[hole_pos] = value

InsertionSort(A)

print(A)
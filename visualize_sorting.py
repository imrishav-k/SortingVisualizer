import pygame, time, random

A = [random.randint(1,250) for i in range(1, 160)]


#Sorting Algorithms
def BubbleSort(A, rect, window, clock):
	n = len(A)
	for i in range(n-1):
		for j in range(n-i-1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				DisplayArr(A, rect, window)
				clock.tick(120)
				pygame.display.update()

def SelectionSort(A, rect, window, clock):
	n = len(A)
	for i in range(n):
		ind = i
		for j in range(i+1, n):
			if A[ind] > A[j]:
				ind = j
		A[i], A[ind] = A[ind], A[i]
		DisplayArr(A, rect, window)
		clock.tick(5)
		pygame.display.update()

def InsertionSort(A, rect, window, clock):
	n = len(A)
	for i in range(1, n):
		value = A[i]
		hole_pos = i

		while hole_pos > 0 and A[hole_pos - 1] > value:
			A[hole_pos] = A[hole_pos - 1]
			hole_pos = hole_pos - 1
		A[hole_pos] = value
		DisplayArr(A, rect, window)
		clock.tick(20)
		pygame.display.update()

def partition(A, low, high):
	pivot = A[high]
	i = low - 1

	for j in range(low, high):
		if A[j] <= pivot:
			i = i + 1
			A[i], A[j] = A[j], A[i]

	A[i + 1], A[high] = A[high], A[i + 1]
	return i + 1


def QuickSort(A, low, high, rect, window, clock):
	if low < high:
		p = partition(A, low, high)
		QuickSort(A, low, p - 1, rect, window, clock)

		DisplayArr(A, rect, window)
		clock.tick(40)
		pygame.display.update()

		QuickSort(A, p + 1, high, rect, window, clock)

		DisplayArr(A, rect, window)
		clock.tick(40)
		pygame.display.update()

def DisplayArr(Arr, rect, window):
	window.fill((255,255,255))
	count = 0
	pos = (5,50)
	for rect_height in Arr:	
		rect = pygame.transform.scale(rect, (3, rect_height))
		pos = (5+count, 500 - rect_height)
		window.blit(rect, pos)
		count += 5

def main_function():
	pygame.init()

	window = pygame.display.set_mode((800,600))
	rect = pygame.image.load("rectangle.jpg")

	white = (255,255,255)
	window.fill(white)
	clock = pygame.time.Clock()

	running = True

	while running:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				running = False

		# QuickSort(A, 0, len(A)-1, rect, window, clock)
		# InsertionSort(A, rect, window, clock)
		# SelectionSort(A, rect, window, clock)
		BubbleSort(A, rect, window, clock)
	pygame.quit()

if __name__ == "__main__":
	main_function()

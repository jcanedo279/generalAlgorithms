import math

def insertionSort(l, reverse = False):
	## Iterate over elements 1:n
	for i in range(1, len(l)):
		currentElement = l[i]
		j = i-1
		if reverse:
			## Sort in reverse
			while(j >= 0) and (l[j] < currentElement):
				l[j+1] = l[j]
				j += -1
		else:
			## Sort regularly
			while(j >= 0) and (l[j] > currentElement):
				l[j+1] = l[j]
				j += -1
		l[j+1] = currentElement
	return l
	

testList = [9, 8, 2, 3, 4, 5, 6, 7, 1, 0]
print(insertionSort(testList, True))

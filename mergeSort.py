import math

def mergeSort(l):
	return mergeSortRecurrer(l, 0, len(l)-1)

def mergeSortRecurrer(l, p, r):
	if r-p > 0:
		## p, q, r
		q = math.floor((p+r)/2)
		mergeSortRecurrer(l, p, q)
		mergeSortRecurrer(l, q+1, r)
		merge(l, p, q, r)
		
def merge(l, p, q, r):
	## A = l[p, r+1] comprises two lists
	## left and right who are each sorted
	## and to be merged
	left = l[p:q+1]
	left.append(float("inf"))
	right = l[q+1:r+1]
	right.append(float("inf"))
	
	i, j = 0, 0
	currLeft, currRight = left[i], right[j]
	for k in range(p, r+1):
		## Iterate over elements of A
		if currLeft <= currRight and currLeft != float("inf"):
			l[k] = currLeft
			i += 1
			currLeft = left[i]
		elif currRight != float("inf"):
			l[k] = currRight
			j += 1
			currRight = right[j]


l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
mergeSort(l)
print(l)

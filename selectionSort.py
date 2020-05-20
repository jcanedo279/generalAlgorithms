def selectionSort(l, reverse=False):
	minElement = min(l)
	maxElement = max(l)
	n = len(l)
	
	i = 0;
	while maxElement != minElement:
		l.remove(maxElement)
		if not reverse:
			l.insert(n-i-1, maxElement)
			maxElement = max(l[:n-i-1])
		else:
			l.insert(i, maxElement)
			maxElement = max(l[i+1:])
		i += 1
	return l

l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(selectionSort(l))

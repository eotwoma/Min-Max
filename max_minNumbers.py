def find_maxmin(alist):
	alist.sort()
	if alist[0] == alist[-1]:
		return [len(alist)]
	else:
		return [alist[0], alist[-1]]
		

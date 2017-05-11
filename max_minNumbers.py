def find_maxmin(alist):

	result = []
	mn = min(alist)
	mx = max(alist)
	
	if min(alist) == max(alist):
		#append the number of elements
		result.append(len(alist))
	else:
		result.append(mn)
		result.append(mx)
	return result



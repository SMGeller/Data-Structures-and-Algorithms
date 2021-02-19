def getKey(item):
	return item[2]

def jobSched(jobs, n):
	
	#Sort jobs in decreasing order of profit
	sort = sorted(jobs, key=getKey, reverse=True)
	
	#initilize tracking array
	slots = [False] * n
	result = [None] * n

	for x in sort:

		for j in range(min(n-1,x[1] -1), -1, -1):
			
			if slots[j] is False:
				slots[j] = True
				result[j] = x[0]
				break

	print(result)

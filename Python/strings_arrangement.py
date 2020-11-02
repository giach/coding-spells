def str_diff(w1, w2):
	n = len(w1)
	if(n == 2):
		s = set(list(w1[0:2] + w2[0:2]))
		print(s)
		if len(s) > 3:
			return -10
		if len(s) == 2 or len(s) == 3:
			return 1
		if len(s) < 2:
			return 0
	count = 0
	for i in range(n-2):
		s = set(list(w1[i:i+2] + w2[i:i+2]))
		if len(s) > 2:
			return -10
		if len(s) == 2:
			count += 1

	return count



print(str_diff('za', 'zb'))
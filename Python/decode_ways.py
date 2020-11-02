from collections import defaultdict

def numDecodings(s):
	cache = defaultdict(int)
	cache[len(s)] = 1 # Empty string is 1 valid encoding

	for i in reversed(range(len(s))):
		if s[i].startswith('0'):
			cache[i] = 0
		elif i == len(s) - 1:
			cache[i] = 1
		else:
			if int(s[i:i + 2]) <= 26:
				cache[i] = cache[i + 2]
			cache[i] += cache[i + 1]
		print(cache, s[i], i)

	return cache[0]



def isUgly(num):
	num = -num if num < 0 else num
 	if num == 1:
 		return False

 	notDiv = lambda x, p: False if x % p == 0 else True

	for i in range(2, int(num /2) + 1):
		if num % i == 0 and notDiv(i, 2) and notDiv(i, 3) and notDiv(i, 5):
			return False
	return True


print(numDecodings("10122110"))
# print(isUgly(2147483648))
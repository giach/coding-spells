def climbingstairs(n):
	arr = []

	arr.append(1)
	arr.append(2)

	for k in range(2, n):
		v = arr[k-1] + arr[k-2]
		arr.append(v)

	print(arr[-1])


def fancyClimbingStairs(n):
	a, b = 1, 0

	for _ in range(n):
		a, b = a + b, a

	print(a)

climbingstairs(2)
fancyClimbingStairs(4)
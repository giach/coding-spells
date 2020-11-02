def lcs(s1, s2):
	if not (s1 and s2):
		return 0

	if s1[-1] == s2[-1]:
		return 1 + lcs(s1[:-1], s2[:-1])
	else:
		return max(lcs(s1[:-1], s2), lcs(s1, s2[:-1]))


print(lcs("aabcf", "azbcd"))
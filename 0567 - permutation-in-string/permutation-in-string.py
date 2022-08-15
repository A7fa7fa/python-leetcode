from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
	
	if len(s1) > len(s2):
		return False

	charsS1 = Counter(s1)
	
	i = 0
	lenS1 = len(s1)
	while (i  <= len(s2) - 1):
		temp = Counter(s2[i : i + lenS1])
		if temp == charsS1:
			return True
		i += 1
	
	return False
		



s1 = "adc"
s2 = "dcda"
res = checkInclusion(s1, s2)
print(res)


s1 = "ab"
s2 = "eidbaooo"
res = checkInclusion(s1, s2)
print(res)

def reorderedPowerOf2(self, n: int) -> bool:
	if n == 1:
		return True
	
	nStr = str(n)
	nCounter = Counter(nStr)
	
	powStr = 1
	while  len(str(powStr)) <= len(nStr):
		if len((str(powStr))) < len(nStr):
			powStr *= 2
		else:
			powCounter = Counter(str(powStr))
			
			if powCounter == nCounter:
				return True
			powStr *= 2
	
	return False
	
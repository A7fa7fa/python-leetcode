def reverse(self, x: int) -> int:
	if x >= 0:
		res = int("".join(str(x)[::-1]))
	else:
		res = str(x)[1:]
		res = "".join(str(res)[::-1])
		res = f"-{res}"
	
	if int(res) in range(-2**31, 2**31-1):
		return int(res)
	else:
		return 0

def climbStairs( n: int) -> int:
	
	if n == 1:
		return 1
	
	steps = [0 for _ in range(n)]

	position = 0

	while position < n:
		if position == 0:
			steps[position] = 1
		elif position == 1:
			steps[position] = steps[position - 1] + 1
		else:
			steps[position] = steps[position - 1] + steps[position - 2]
		
		position += 1

	return steps[-1]

res = climbStairs(3)
print(res)
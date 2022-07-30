
def binarySeach( row: list[int], start: int, end: int):
	middle = ((end - start) // 2)  + start
	print("stack", start, end)
	if end - start == 1:
		# only 0 in list
		if row[start] == 0:
			return start - 1
		# only 1 in list
		if row[end] == 1:
			return end
		# start is last 1 in list
		else:
			return start

	# less soldiers
	if row[middle] == 0:
		return binarySeach(row, start, middle)
	# more soldiers
	else:
		return binarySeach(row, middle, end)      

def kWeakestRows( mat: list[list[int]], k: int) -> list[int]:	
	result = []
	
	for idx, row in enumerate(mat):            
		lastSoldierIdx = binarySeach(row, 0, len(row) - 1)
		result.append((lastSoldierIdx + 1, idx))
		
	result.sort(key=lambda x: x[0])
	return [el[1] for el in result][:k]
		

if __name__ == "__main__":
	mat = [[1,0],[0,0],[1,0]]
	k = 2
	res = kWeakestRows(mat=mat, k=k)
	print(res)

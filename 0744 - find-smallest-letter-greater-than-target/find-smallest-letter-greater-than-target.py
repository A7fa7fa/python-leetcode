def nextGreatestLetter(letters: list[str], target: str) -> str:
	
	start = 0
	end = len(letters) - 1
	
	while start < end:
		
		mid = (start + end) // 2

		# if ord(letters[mid]) == ord(target):
		# 	return letters[mid + 1]
		
		if ord(letters[mid]) > ord(target):
			end = mid
		else:
			start = mid + 1
		print(start, mid, end)
	
	if ord(letters[-1]) <= ord(target):
		return letters[0]
	
	return letters[start]

letters = ["c","f","j"]
target = "a"
res = nextGreatestLetter(letters, target)
print(res)

letters = ["c","f","j"]
target = "c"
res = nextGreatestLetter(letters, target)
print(res)

letters = ["c","f","j"]
target = "d"
res = nextGreatestLetter(letters, target)
print(res)

letters = ["c","f","j"]
target = "j"
res = nextGreatestLetter(letters, target)
print(res)

letters = ["c","f","j"]
target = "f"
res = nextGreatestLetter(letters, target)
print(res)

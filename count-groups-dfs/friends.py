def findFriends(idxSender: int, mat: list[list[int]], visited, setOfFriends):
	for idxFriend, friend in enumerate(mat[idxSender]):
		# friend is not sender itself
		if idxFriend == idxSender:
			continue
		# has gifted and friend has not been visited before
		if friend == 1 and idxFriend not in visited:
			# new group
			setOfFriends.add(idxFriend)
			setOfFriends.add(idxSender)
			visited.add(idxSender)
			findFriends(idxFriend, mat, visited, setOfFriends)



def countGroups(mat: list[int]):
	

	groupCount = 0

	visited = set()

	# for every person. check ever other person but only if not been visited before  
	for idxSender in range(len(mat)):
		setOfFriends = set()
		if idxSender not in visited:
			findFriends(idxSender, mat, visited, setOfFriends)

			# if setOfFriends is not empty. group of friend has been found. 
			# so increment counter and reset setOfFriends
			if len(setOfFriends) > 0:
				groupCount += 1
				print("group", setOfFriends)
				setOfFriends = set()
	
	
	return groupCount
				




mat = [
		[1, 1, 1, 1, 1, 1],
		[1, 1, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 1, 1]]
mat2 = [
		[1, 1, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0],
		[0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 1]
]

print(countGroups(mat2))
# CyclicRotation
# Rotate an array to the right by a given number of steps. 

def solution(A, K):
	# write a right rotation function
	def rotateRight(array_to_rotate):
		# insert placeholder to push
		array_to_rotate.insert(0, 'x')
		# get last element
		new_first = array_to_rotate.pop()
		# put in placeholder
		array_to_rotate[0] = new_first
		return array_to_rotate

	# check for N = 0
	if A == []:
		return []
	# rotate K times
	new_array = A
	for _ in range(K):
		new_array = rotateRight(new_array)

	return new_array
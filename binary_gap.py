def solution(N):
	# convert the integer to binary representation
	bin_string = format(N, 'b')
	# variable for longest gap
	longest_gap = 0
	# get strings of zeros in a list
	zero_strings = bin_string.split('1')
	# if the last digit is a 0, then remove the last element
	if bin_string[-1] == '0':
		zero_strings.pop()
	for string in zero_strings:
		# check length
		gap = len(string)
		if gap > longest_gap:
			longest_gap = gap
	# return result
	return longest_gap
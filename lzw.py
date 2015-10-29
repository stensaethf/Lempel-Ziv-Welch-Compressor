'''
lzw.py
Frederik Roenn Stensaeth
10.28.15

A Python implementation of the Lempel-Ziv-Welch compression algorithm.
'''

# Any imports?

def compress(text):
	"""
	compress() takes a string and compresses it using the LZW algorithm.
	Returns the compressed string in the form of a list of integers.

	@params: string to be compressed.
	@return: compressed string (list of ints).
	"""
	# Creates a list that will hold the integers after compression of the
	# string.
	compressed_lst = []

	# Makes the dictionary to hold our values we map to.
	table = {}
	for i in range(256):
		table[chr(i)] = i

	value = ''
	index = 0
	# Loop over each individual character in the text and keep track of where
	# in the string you are (using the value index). Value keeps track of the
	# longest substring you have seen that is in your table.
	for char in text:
		total = value + char
		index += 1
		# If we have seen total before we want to make it our value (aka we
		# want to remember it) and move on to the next character. However,
		# we also need to check if we have reached the end of the string. If
		# we have reached the end, we add the total to our compressed list.
		if total in table:
			if index == len(text):
				compressed_lst.append(table[total])
			value = total
		# However, if we have not seen total before, we add value (the
		# substring we had remembered) to the ditionary and we add total
		# to the dictionary (because we have not seen it before). We then
		# move on to remembering the most recent character.
		else:
			compressed_lst.append(table[value])
			table[total] = len(table)
			value = char
		# print(total) # For testing purposes.

	return compressed_lst

def decompress(compressed_lst):
	"""
	decompress() takes a list of integers and decompresses it using the LZW
	algorithm. Returns the decompressed string.

	@params: compressed string (list of ints).
	@return: decompressed string.
	"""
	# Code
	# Xx

def main():
	# Code
	print(compress('abananabanana'))


if __name__ == '__main__':
	main()
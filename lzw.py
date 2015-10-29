'''
lzw.py
Frederik Roenn Stensaeth
10.28.15

A Python implementation of the Lempel-Ziv-Welch compression algorithm.
'''

# Any imports?
import sys

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
		# print total
		index += 1
		# If we have seen total before we want to make it our value (aka we
		# want to remember it) and move on to the next character. However,
		# we also need to check if we have reached the end of the string. If
		# we have reached the end, we add the total to our compressed list.
		if total in table:
			value = total

		# However, if we have not seen total before, we add value (the
		# substring we had remembered) to the ditionary and we add total
		# to the dictionary (because we have not seen it before). We then
		# move on to remembering the most recent character.
		else:
			compressed_lst.append(table[value])
			table[total] = len(table)
			value = char

		if index == len(text):
			compressed_lst.append(table[value])
		# print(total) # For testing purposes.

	return compressed_lst

def decompress(compressed_lst):
	"""
	decompress() takes a list of integers and decompresses it using the LZW
	algorithm. Returns the decompressed string.

	@params: compressed string (list of ints).
	@return: decompressed string.
	"""
	# We start by reconstructing the dictionary we used to compress the
	# string. However, now the keys are the integers and the values are the 
	# strings.
	table = {}
	for i in range(256):
		table[i] = chr(i)

	prev = str(chr(compressed_lst[0]))
	compressed_lst = compressed_lst[1:]
	decompressed_str = prev
	# Loops over element in the compressed list so that we can decompress it.
	# If an element does not exist in our table it must be premature and
	# hence, the list we were given is invalid --> error.
	# If an element is in the list we retrieve it and add it to our solution.
	# And then make sure to add a new value to our table, which is the
	# previous element plus the first letter of the current string.
	for element in compressed_lst:
		if element not in table:
			printError(1)
		elif element in table:
			# print(element)
			string = table[element]
		else:
			printError(1)
		decompressed_str += string

		# Constructs new values to add to our table by taking the previous
		# string and adding the first letter of the current string to it.
		table[len(table)] = prev + string[0]

		prev = string

	return decompressed_str

def printError(num):
	if num == 1:
		print('Error. Invalid compressed list given to decompress().')
	else:
		print('Error.')
	print('Usage: $ lzw.py <string to be compressed> | <compressed list>')
	sys.exit()

def main():
	comp = compress('abananabanana')
	print(comp)
	decomp = decompress(comp)
	print(decomp)

	# if len(sys.argv) != 1:
	# 	printError(0)
	# if sys.argv.type == list:
	# 	Xx
	# elif sys.argv.type == str:
	# 	Xx


if __name__ == '__main__':
	main()
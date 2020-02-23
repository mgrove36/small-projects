# import module to sort characters in order of frequency
from collections import Counter

# function to find path of desired character
def find_node(nodes, target_character):
    for index, item in enumerate(nodes):
        if item == target_character:
			# return its path
            return [str(index)]
        if isinstance(item, (list, tuple)):
			# run this function again to dig further into the nested items
            path = find_node(item, target_character)
			# if desired character is found, return its path
            if path:
                return [str(index)] + path
	# if desired character not found, return empty list
    return []

def encode(txt):
	# list of tuples in descending order of frequency: (character, frequency)
	info = Counter(txt).most_common()
	# change the list into ascending order
	info.reverse()
	# list for character tuples
	nodes = []
	# list for node usage frequencies
	frequencies = []

	# copy nodes and their usage frequencies to the dedicated lists
	for item in info:
		nodes.append(item[0])
		frequencies.append(item[1])

	# repeat until only one top-level node exists
	while len(nodes) > 2:
		# combine two least frequent characters' nodes into a new tuple node, containing the old nodes (old_node_1, old_node_2)
		new_node = (nodes[0], nodes[1])
		# combine two least frequent characters' frequencies into a total frequency, to be used at the top level of the list of nodes
		new_frequency = frequencies[0] + frequencies[1]
		#  remove nodes that have been nested inside the new node
		del nodes[0:2]
		#  remove frequencies that have been summed and added to the new frequency
		del frequencies[0:2]
		
		# find index of the last node with a frequency below that of the new node

		# if the largest frequency is smaller than the new one, place the new node at the end of the list
		if (frequencies[-1] < new_frequency):
			i = -1
		else:
			# loop over every frequency
			for index, frequency in enumerate(frequencies):
				if (frequency >= new_frequency):
					# record the index to insert the frequency at
					i = index
					break
		
		# insert the new node and frequency in their rightful positions, maintaining ascending order of frequency
		nodes.insert(i, new_node)
		frequencies.insert(i, new_frequency)

	print(f"Nodes: {nodes}")

	# encrypted text
	output = ""

	for char in txt:
		# find its path and add it to the encrypted text
		output += "".join(find_node(nodes, char))

	print(f"Encoded message: {output}")
	
	return [output, nodes]

def decode(txt, nodes):
	# string to hold decoded message
	output = ""
	# replicate nodes, for looping over and editing with the first part of the code
	node = nodes
	for digit in txt:
			# get the node with the corresponding index
			node = node[int(digit)]
			# if the retrieved node isn't a tuple (i.e. it isn't a parent node)
			if (not isinstance(node, tuple)):
				output += node
				# replace the retrieved node with the whole tree again, for looping over and editing with the next part of the code
				node = nodes

	print(f"Decoded message: {output}")
	return output

encoding = encode(input("Text: "))
decode(encoding[0], encoding[1])

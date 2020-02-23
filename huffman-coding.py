from collections import Counter

# function to find path of desired character
def find_node(nodes, target_character):
	# for each item in nodes
    for index, item in enumerate(nodes):
		# if item is desired character, return the path to it
        if item == target_character:
            return [str(index)]
		# if the item is a list or tuple
        if isinstance(item, (list, tuple)):
			# run this function again to dig further into the nested items
            path = find_node(item, target_character)
			# if desired character is found, return its path
            if path:
                return [str(index)] + path
	# if desired character not found, return empty list
    return []

# retrieve text to encode
txt = input("Text: ")

# create list of tuples in descending order of frequency: (character, frequency)
info = Counter(txt).most_common()
# change the list into ascending order
info.reverse()
# create list for character tuples
nodes = []
# create list for node usage frequencies
frequencies = []

# copy nodes and their usage frequencies to the dedicated lists
for item in info:
	nodes.append(item[0])
	frequencies.append(item[1])

# repeat until only one top-level node exists
while len(nodes) > 1:
	# combine two least frequent characters' nodes into a new tuple node, containing the old nodes (old_node_1, old_node_2)
	new_node = (nodes[0], nodes[1])
	# combine two least frequent characters' frequencies into a total frequency, to be used at the top level of the list of nodes
	new_frequency = frequencies[0] + frequencies[1]
	#  remove nodes that have been nested inside the new node
	del nodes[0:2]
	#  remove frequencies that have been summed and added to the new frequency
	del frequencies[0:2]
	
	# find index of last node with frequency below that of the new node
	# if the largest frequency is smaller than the new one, place the new node at the end of the list
	if (frequencies[-1] < new_frequency):
		i = -1
	else:
		# else, loop over every frequency
		for index, item in enumerate(frequencies):
			# if the frequency is greater than or equal to the new frequency
			if (item >= new_frequency):
				# record the index to insert the frequency at
				i = index
				# stop looping
				break
	
	# insert the new node in its rightful position, maintaining ascending order of frequency
	nodes.insert(i, new_node)
	# insert the new frequency in its rightful position, maintaining ascending order of frequency
	frequencies.insert(i, new_frequency)

# print all nodes
print("Nodes: %s" % nodes)

# encrypted text
output = ""

# for every character in the text to be encrypted
for char in txt:
	# find its path and add it to the encrypted text
	output += "".join(find_node(nodes, char))

# print encrypted message
print("Encrypted message: %s" % output)

# function to sum integers via recursion
def total(numbers):
	# if recursion not needed due to too few items
	if len(numbers) == 1:
		return numbers[0]
	return numbers[0] + total(numbers[1:])

# function to find if number is prime via recursion
def prime(number, divisor = None):
	# create initial divisor, only if it doesn't exist
	if not divisor:
		# divide by two because all factors are duplicated - searching through all numbers smaller than the given number would search all factor pairs twice
		# floor divide because if it's not an integer, it's not a valid factor - so can be ignored
		# if rounded up, the number's compliment will appear again later, in the reverse of the factor pair
		divisor = number // 2
	# number isn't a prime if less than two, or if it has a factor that's greater than one
	if (number <= 1) or (divisor > 1 and number % divisor == 0):
		return False
	# all prime have been checked, and none are factors of the number
	elif (divisor <= 1):
		return True
	else:
		return prime(number, divisor - 1)

# function for binary search via recursion
def search(item, list):
	# get middle index (-1 accounts for zero-based indexing)
	midpoint = (len(list) + 1) // 2 - 1
	# item found
	if item == list[midpoint]:
		return True
	# all of list searched and item not found
	elif (len(list) == 1):
		return False
	# item is larger than the middle item, so must be in the larger half of the list
	elif item > list[midpoint]:
		return search(item, list[midpoint + 1:])
	# item is smaller than the middle item, so must be in the smaller half of the list
	else:
		return search(item, list[:midpoint])
array = [7, 2, 5, 8, 0,1,2,3,4,5,6,7]
swapped = True
print("Original array:", array)

while swapped:
    swapped = False
    for i, item in enumerate(array):
        if i != len(array) - 1:
            if item > array[i + 1]:
                array[i] = array[i + 1]
                array[i + 1] = item
                swapped = True

print("New array:", array)
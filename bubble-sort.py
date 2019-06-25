array = [24, 10, 40, 28, 31, 9, 29, 42, 39, 19, 18, 37, 11, 14, 49, 47, 22, 16, 38, 6, 4, 27, 21, 48, 35, 23, 17, 1, 44, 25, 41, 2, 46, 30, 8, 50, 32, 5, 20, 33, 34, 26, 36, 12, 43, 15, 45, 7, 3, 13]
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

print("New array:     ", array)
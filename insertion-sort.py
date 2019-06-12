array = [24, 10, 40, 28, 31, 9, 29, 42, 39, 19, 18, 37, 11, 14, 49, 47, 22, 16, 38, 6, 4, 27, 21, 48, 35, 23, 17, 1, 44, 25, 41, 2, 46, 30, 8, 50, 32, 5, 20, 33, 34, 26, 36, 12, 43, 15, 45, 7, 3, 13]
print("Original array:", array)
for i in range(0, len(array)):
    j = 0
    while array[i] > array[j]:
        j += 1
    if (j - 1) != i:
        array.insert(j, array.pop(i))
print("New array:", array)
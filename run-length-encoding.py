def sameChar(chars):
	if len(chars) < 2 or chars[0] != chars[1]:
		return 1
	else:
		return 1 + sameChar(chars[1:])

def RLE(uncompressed):
	total_chars = 0
	compressed = []

	while total_chars < len(uncompressed):
		char_count = sameChar(uncompressed[total_chars:])
		compressed.append(f"{uncompressed[total_chars]} {char_count}")
		total_chars += char_count
	
	return " ".join(compressed)


print(RLE(input("Uncompressed text: ")))

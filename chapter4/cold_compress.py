# DMOJ problem ccc19j3

n = int(input())

for _ in range(n):
	line = input()
	size = len(line)
	output = ''
	i = 0

	while i < size:
		current_count = 1
		current_char = line[i]
		while i < size - 1 and current_char == line[i + 1]:
			current_count += 1
			i += 1
		output = output + str(current_count) + ' ' + str(current_char) + ' '
		i += 1

	print(output)
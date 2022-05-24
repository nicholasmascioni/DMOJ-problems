# DMOJ problem coci18c3p1

word = input()

block_count = 0
h_count = 0
o_count = 0
n_count = 0
i_count = 0

for char in word:
	if char == 'H' and h_count != 1:
		h_count += 1
	elif char == 'O' and h_count == 1 and o_count != 1:
		o_count += 1
	elif char == 'N' and h_count == 1 and o_count == 1 and n_count != 1:
		n_count += 1
	elif char == 'I' and h_count == 1 and o_count == 1 and n_count == 1:
		block_count += 1
		h_count = 0
		o_count = 0
		n_count = 0

print(block_count)
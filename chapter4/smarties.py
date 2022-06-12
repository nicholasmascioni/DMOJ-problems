# DMOJ problem ecoo15r1p1

for inputs in range(10): # When the program is tested on DMOJ, 10 test cases are used

	time = 0

	handful = 0

	orange = 0
	blue = 0
	green = 0
	yellow = 0
	pink = 0
	violet = 0
	brown = 0
	red = 0
	
	line = ''

	while line != 'end of box':
		line = input()

		if line == 'orange':
			orange += 1
		elif line == 'blue':
			blue += 1
		elif line == 'green':
			green += 1
		elif line == 'yellow':
			yellow += 1
		elif line == 'pink':
			pink += 1
		elif line == 'violet':
			violet += 1
		elif line == 'brown':
			brown += 1
		elif line == 'red':
			red += 1

	smarties = [orange, blue, green, yellow, pink, violet, brown]

	# Hand holds 7 smarties max, adding 6 accounts for hands that are not full

	for smartie in smarties:
		handful += ((smartie + 6) // 7)

	# Red smarties are eaten one at a time, at a rate of 16 seconds per smartie	

	time = (handful * 13) + (red * 16)

	print(time)
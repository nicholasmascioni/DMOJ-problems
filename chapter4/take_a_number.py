# DMOJ problem ecoo13r1p1

n = int(input())

end = False

late_students = 0
in_line = 0

while end != True:
	line = input()

	if line == 'EOF':
		end = True

	elif line == 'TAKE':
		late_students += 1
		in_line += 1
		n += 1
		if n == 1000: # checks if the tickets have run out
			n = 1
	elif line == 'SERVE':
		in_line -= 1
	elif line == 'CLOSE':
		print(late_students, in_line, n)
		late_students = 0
		in_line = 0
	
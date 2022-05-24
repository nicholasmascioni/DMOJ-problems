# DMOJ problem ccc11s2

n = int(input())

correct_answers = 0

lines = []

for _ in range((2 * n)):
	line = input()
	lines.append(line)	

for i in range(len(lines) - n):
	if lines[i] == lines[i + n]:
		correct_answers += 1

print(correct_answers)
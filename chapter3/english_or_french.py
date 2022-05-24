# DMOJ problem ccc11s1

n = int(input())

t_count = 0
s_count = 0

for i in range(n):
	line = input().lower()
	for j in range(len(line)):
		if line[j] == 't':
			t_count += 1
		elif line[j] == 's':
			s_count += 1

if t_count > s_count:
	print('English')
else:
	print('French')

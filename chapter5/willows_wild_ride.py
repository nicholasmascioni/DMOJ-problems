# DMOJ problem ecoo18r1p1

for dataset in range(10): # Input contains 10 datasets
	data = input().split()

	for i in range(2):
		data[i] = int(data[i])

	
	T = data[0]
	N = data[1]
	
	time = 0

	for i in range(N):
		state = input()
		if state == 'B':
			time += T - 1
		else:
			if time > 0:
				time -= 1
	print(time)

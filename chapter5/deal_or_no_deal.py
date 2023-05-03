# DMOJ problem ccc07j3

n = int(input())

briefcases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

for _ in range(n):
	open = int(input())
	if open == 1:
		briefcases.remove(100)
	elif open == 2:
		briefcases.remove(500)
	elif open == 3:
		briefcases.remove(1000)
	elif open == 4:
		briefcases.remove(5000)
	elif open == 5:
		briefcases.remove(10000)
	elif open == 6:
		briefcases.remove(25000)
	elif open == 7:
		briefcases.remove(50000)
	elif open == 8:
		briefcases.remove(100000)
	elif open == 9:
		briefcases.remove(500000)
	elif open == 10:
		briefcases.remove(1000000) 

offer = int(input())

average = sum(briefcases) / len(briefcases)

if offer > average:
	print('deal')
else:
	print('no deal')

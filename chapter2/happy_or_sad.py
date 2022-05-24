# DMOJ problem ccc15j2

line = input()

happy = ':-)'
sad = ':-('

happy_count = line.count(happy)
sad_count = line.count(sad)

if (happy_count == 0 and sad_count == 0):
	print('none')
elif happy_count == sad_count:
	print('unsure')
elif happy_count > sad_count:
	print('happy')
elif sad_count > happy_count:
	print('sad')
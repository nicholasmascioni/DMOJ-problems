# DMOJ problem ccc02j2

finish = False

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

while finish == False:
	word = input()
	if word == 'quit!':
		finish = True
	elif (len(word) > 4) and (word[-3] not in vowels) and (word[-2:] == 'or'):
		word = word[:-2] + 'our'
		print(word)
	else:
		print(word)
	
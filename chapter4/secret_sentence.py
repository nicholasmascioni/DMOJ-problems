# DMOJ problem coci08c3p2

sentence = input()

result = ''
i = 0

while i < len(sentence):
	result += sentence[i]
	if sentence[i] in 'aeiou': # check for a vowel
		i += 3
	else:
		i += 1

print(result)
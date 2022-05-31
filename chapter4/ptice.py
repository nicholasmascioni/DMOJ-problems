# DMOJ problem coci08c1p2

n = int(input())
solutions = input()

adrian = '' # sequence A,B,C,A,B,C, ...
bruno = '' # sequence B,A,B,C,B,A,B,C, ...
goran = '' # sequence C,C,A,A,B,B,C,C,A,A,B,B, ...

adrian_correct = 0
bruno_correct = 0
goran_correct = 0

i = 0

while i < n:
	if i % 3 == 0:
		adrian += 'A'
		goran += 'CC'
		i += 1
	elif i % 3 == 1:
		adrian += 'B'
		goran += 'AA'
		i += 1
	elif i % 3 == 2:
		adrian += 'C'
		goran += 'BB'
		i += 1

j = 0

while j < n:
	if j % 2 == 0:
		bruno += 'BA'
		j += 1
	else:
		bruno += 'BC'
		j += 1

while len(bruno) > n:
	bruno = bruno[:-1] # removes the last character from the string

while len(goran) > n:
	goran = goran[:-1]

for k in range(n):
	if adrian[k] == solutions[k]:
		adrian_correct += 1
	if bruno[k] == solutions[k]:
		bruno_correct += 1
	if goran[k] == solutions[k]:
		goran_correct += 1

correct_answers = [adrian_correct, bruno_correct, goran_correct]

m = max(correct_answers) # returns highest test score

print(m)

if adrian_correct == m:
	print('Adrian')
if bruno_correct == m:
	print('Bruno')
if goran_correct == m:
	print('Goran')


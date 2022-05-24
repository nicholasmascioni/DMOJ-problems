# DMOJ problem coci18c4p1

original = input()
n = int(input())

current_wizard = original
wizard_count = 1
obeyed = [current_wizard]

for i in range(n):
	duel = input()
	if (current_wizard in duel) and (duel[2] == current_wizard): # current wizard loses
		current_wizard = duel[0] # wand obeys new wizard
		if current_wizard not in obeyed:
			obeyed.append(current_wizard)
			wizard_count += 1

print(current_wizard)
print(wizard_count)
		
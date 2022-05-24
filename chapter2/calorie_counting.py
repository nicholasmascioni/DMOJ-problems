# DMOJ problem ccc06j1

calorie_total = 0

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

if burger == 1:
	calorie_total += 461
elif burger == 2:
	calorie_total += 431
elif burger == 3:
	calorie_total += 420
else:
	calorie_total += 0

if side == 1:
	calorie_total += 100
elif side == 2:
	calorie_total += 57
elif side == 3:
	calorie_total += 70
else:
	calorie_total += 0

if drink == 1:
	calorie_total += 130
elif drink == 2:
	calorie_total += 160
elif drink == 3:
	calorie_total += 118
else:
	calorie_total += 0

if dessert == 1:
	calorie_total += 167
elif dessert == 2:
	calorie_total += 266
elif dessert == 3:
	calorie_total += 75
else:
	calorie_total += 0

print('Your total Calorie count is ' + str(calorie_total) + '.')
# DMOJ problem dmopc16c1p0

width = int(input())
cheese = int(input())

satisfaction = ''

if (width == 3 and cheese >= 95):
	satisfaction = 'absolutely'
elif (width == 1 and cheese <= 50):
	satisfaction = 'fairly'
else:
	satisfaction = 'very'

print('C.C. is ' + satisfaction + ' satisfied with her pizza.')
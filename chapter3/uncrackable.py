# DMOJ problem wc17c3j3

password = input()

# must be between 8 and 12 characters long, at least: 
# 3 lowercase letters, 2 uppercase letters, 1 digit

lower_count = 0
upper_count = 0
digit_count = 0

for char in password:
	if char.isupper():
		upper_count += 1
	elif char.islower():
		lower_count += 1
	elif char.isdigit():
		digit_count += 1

if ((len(password) >= 8) and (len(password) <= 12) and
(lower_count >= 3) and (upper_count >= 2) and (digit_count >= 1)):
	print('Valid')
else:
	print('Invalid')
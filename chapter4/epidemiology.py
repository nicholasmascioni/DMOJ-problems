# DMOJ problem ccc20j2

P = int(input()) # Total which should be surpassed
N = int(input()) # Number of people with disease on day 0
R = int(input()) # Other people infected the next day

total = N
day = 0

while total <= P:
	day += 1
	total += N * R**day
	

print(day)
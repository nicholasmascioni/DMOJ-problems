# DMOJ problem ccc07j1

bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

if bowl1 > bowl2:
	bowl1,bowl2 = bowl2,bowl1
if bowl1 > bowl3:
	bowl1,bowl3 = bowl3,bowl1
if bowl2 > bowl3:
	bowl2,bowl3 = bowl3,bowl2

print(bowl2)
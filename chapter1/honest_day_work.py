# DMOJ problem wc18c3j1

paint = int(input()) # P
required = int(input()) # B
value = int(input()) # D

caps = paint // required # rounds down, can't have a partial cap

paint_used = caps * required

cap_revenue = value * caps
leftover = paint - paint_used

total = cap_revenue + leftover

print(total)
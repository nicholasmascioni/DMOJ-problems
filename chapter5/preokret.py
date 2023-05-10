# DMOJ problem coci18c2p1
HALF_TIME = 1440

teamA_times = []
teamB_times = []

teamA_points = int(input())
for _ in range(teamA_points):
    teamA_times.append(int(input()))

teamB_points = int(input())
for _ in range(teamB_points):
    teamB_times.append(int(input()))

# Part 1

half_score = 0

for time in teamA_times:
    if time <= HALF_TIME:
        half_score += 1

for time in teamB_times:
    if time <= HALF_TIME:
        half_score += 1

print(half_score)

# Part 2

score = [0, 0] # Team A, Team B

turnarounds = 0

prev_leading = ''
current_leading = ''

full_times = []
full_times.extend(teamA_times)
full_times.extend(teamB_times)
full_times.sort()

for time in full_times:
    if time in teamA_times:
        score[0] += 1
    elif time in teamB_times:
        score[1] += 1
    if (score[0] > score[1]) and score[1] != 0: # A overtakes B and B has scored more than once
        current_leading = 'A'
        if (current_leading != prev_leading):
            turnarounds += 1
            prev_leading = current_leading
    elif (score[0] < score[1]) and score[0] != 0: # B overtakes A and A has scored more than once
        current_leading = 'B'
        if (current_leading != prev_leading):
            turnarounds += 1
            prev_leading = current_leading

print(turnarounds)
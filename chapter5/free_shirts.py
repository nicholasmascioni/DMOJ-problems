# DMOJ problem ecoo19r1p1

for dataset in range(10): # Input contains 10 datasets
    line = input().split()
    shirts = int(line[0])
    events = int(line[1])
    days = int(line[2])

    event_days = input().split()

    for day in range(len(event_days)):
        event_days[day] = int(event_days[day])

    laundry_count = 0
    dirty_shirts = 0

    for day in range(1, days+1):
        if dirty_shirts == shirts:
            laundry_count += 1
            dirty_shirts = 0

        if day in event_days:
            shirts += event_days.count(day)

        dirty_shirts += 1

    print(laundry_count)
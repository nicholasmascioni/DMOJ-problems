# DMOJ problem ccc00s2

streams = []

streams_num = int(input())

for _ in range(streams_num):
    streams.append(int(input()))

run = True

while run == True:
    line = int(input())

    if line == 99:
        # Split stream into two
        # Target stream's flow becomes a percentage of itself
        # Rest of the water flows into the new stream to the right
        stream = int(input())
        percent = int(input())

        original_flow = streams[stream-1]
        new_flow = original_flow * percent / 100
        leftover = original_flow - new_flow

        streams[stream-1] = new_flow
        streams.insert(stream, leftover)
    elif line == 88:
        # Remove stream to the right of rejoin and combine it with stream at index rejoin
        rejoin = int(input())

        combine = streams.pop(rejoin)
        streams[rejoin-1] += combine

    elif line == 77:
        run = False

# Round final answers to nearest int and display output on a single line
for stream in streams:
    print(round(stream), end=" ")
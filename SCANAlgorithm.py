# Function to implement SCAN algorithm
def scan(requests, start, direction):
    total_tracks = 200
    current_position = start
    seek_sequence = [start]

    if direction == "outward":
        while True:
            for track in range(current_position, -1, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            if not requests:
                break
            seek_sequence.append(0)
            current_position = 0

            for track in range(current_position + 1, total_tracks):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)

    elif direction == "inward":
        while True:
            for track in range(current_position, total_tracks):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            if not requests:
                break
            seek_sequence.append(total_tracks - 1)
            current_position = total_tracks - 1

            for track in range(current_position - 1, -1, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)

    return seek_sequence, sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))

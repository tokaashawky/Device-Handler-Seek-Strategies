# Function to implement LOOK algorithm
def look(requests, start, direction):
    seek_sequence = [start]
    if direction == "outward":
        while requests:
            for track in range(start, -1, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            for track in range(start + 1, 200):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
    elif direction == "inward":
        while requests:
            for track in range(start, 200):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            for track in range(start - 1, -1, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
    return seek_sequence, sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))

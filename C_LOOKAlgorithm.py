# Function to implement C-LOOK algorithm
def c_look(requests, start, direction):
    total_tracks = 200
    seek_sequence = [start]
    if direction == "outward":
        while requests:
            for track in range(start, -1, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            for track in range(total_tracks - 1, start, -1):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
    elif direction == "inward":
        while requests:
            for track in range(start, total_tracks):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
            for track in range(0, start):
                if track in requests:
                    seek_sequence.append(track)
                    requests.remove(track)
    return seek_sequence, sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))

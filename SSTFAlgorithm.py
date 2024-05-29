# Function to implement SSTF algorithm
def sstf(requests, start):
    seek_sequence = [start]
    while requests:
        closest_track = min(requests, key=lambda x: abs(x - seek_sequence[-1]))
        seek_sequence.append(closest_track)
        requests.remove(closest_track)
    return seek_sequence, sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))

# Function to implement FCFS algorithm
def fcfs(requests, start):
    seek_sequence = [start]
    seek_sequence.extend(requests)
    return seek_sequence, sum(abs(seek_sequence[i] - seek_sequence[i-1]) for i in range(1, len(seek_sequence)))

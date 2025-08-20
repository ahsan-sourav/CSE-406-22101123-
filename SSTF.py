# LAB 6 | Shortest seek time first Scheduling algorithm

def sstf_scheduling(requests, head):
    seek_count = 0
    distance = 0
    cur_head = head
    sequence = []

    while requests:
        closest = min(requests, key=lambda x: abs(x - cur_head))
        distance = abs(closest - cur_head)
        seek_count += distance
        cur_head = closest
        sequence.append(closest)
        requests.remove(closest)

    return seek_count, sequence
# input
requests = [11, 34, 41, 50, 52, 69, 70, 114]
head = 50

seek_count, sequence = sstf_scheduling(requests, head)

print(f"Total Seek Count: {seek_count}")
print(f"Seek Sequence: {sequence}")

# LAB 7 | SCAN Disk Scheduling (direction = left) algorithm

def scan_disk_scheduling(requests, head):
    requests.sort()
    left = []
    right = []

    for request in requests:
        if request < head:
            left.append(request)
        elif request > head:
            right.append(request)

    left.sort(reverse=True)
    right.sort() 

    total_seek_count = 0
    sequence = []

    for i in range(len(left)):
        total_seek_count += abs(head - left[i])
        head = left[i]
        sequence.append(head)

    total_seek_count += abs(head - 0)
    head = 0
    for i in range(len(right)):
        total_seek_count += abs(head - right[i])
        head = right[i]
        sequence.append(head)
    return total_seek_count, sequence

requests_input = input("Enter the request sequence (separated by spaces): ")
requests = list(map(int, requests_input.split()))
head = int(input("Enter the initial head position: "))

seek_count, sequence = scan_disk_scheduling(requests, head)

print(f"Total Seek Count: {seek_count}")
print(f"Sequence of Accessed Tracks: {sequence}")
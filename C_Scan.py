# LAB 8 | C Scan Disk Scheduling CPU Scheduling

n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter requests (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
direction = input("Enter direction (left/right): ").strip().lower()

requests.sort()

left_requests = [r for r in requests if r < head]
right_requests = [r for r in requests if r >= head]

seek_sequence = [head]
total_head_movement = 0
current_position = head

if direction == "right":
    for r in right_requests:
        seek_sequence.append(r)
        total_head_movement += abs(current_position - r)
        current_position = r
    if current_position != disk_size - 1:
        seek_sequence.append(disk_size - 1)
        total_head_movement += abs(current_position - (disk_size - 1))
        current_position = disk_size - 1
    if left_requests:
        seek_sequence.append(0)
        total_head_movement += abs(current_position - 0)
        current_position = 0
    for r in left_requests:
        seek_sequence.append(r)
        total_head_movement += abs(current_position - r)
        current_position = r
else: 
    for r in reversed(left_requests):
        seek_sequence.append(r)
        total_head_movement += abs(current_position - r)
        current_position = r
    if current_position != 0:
        seek_sequence.append(0)
        total_head_movement += abs(current_position - 0)
        current_position = 0
    if right_requests:
        seek_sequence.append(disk_size - 1)
        total_head_movement += abs(current_position - (disk_size - 1))
        current_position = disk_size - 1
    for r in reversed(right_requests):
        seek_sequence.append(r)
        total_head_movement += abs(current_position - r)
        current_position = r
print("\nSeek Sequence: " + " -> ".join(map(str, seek_sequence)))
print("Total Head Movement:", total_head_movement)
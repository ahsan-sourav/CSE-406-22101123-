# LAB 8 | C Scan Disk Scheduling CPU Scheduling

n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter requests (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))
direction = input("Enter direction (left/right): ").strip().lower()

requests.sort()
left = [r for r in requests if r < head]
right = [r for r in requests if r >= head]

seek_sequence = [head]
total_movement = 0
cur = head

if direction == "right":
    for r in right:
        seek_sequence.append(r)
        total_movement += abs(cur - r)
        cur = r
    if cur != disk_size - 1:
        seek_sequence.append(disk_size - 1)
        total_movement += abs(cur - (disk_size - 1))
        cur = disk_size - 1
    for r in reversed(left):
        seek_sequence.append(r)
        total_movement += abs(cur - r)
        cur = r
else:
    for r in reversed(left):
        seek_sequence.append(r)
        total_movement += abs(cur - r)
        cur = r
    if cur != 0:
        seek_sequence.append(0)
        total_movement += abs(cur - 0)
        cur = 0
    for r in right:
        seek_sequence.append(r)
        total_movement += abs(cur - r)
        cur = r

print("Seek sequence:", " -> ".join(map(str, seek_sequence)))
print("Total head movement:", total_movement)
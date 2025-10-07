# LAB 5 | FCFS Disk Scheduling CPU Scheduling

requests = list(map(int, input("Enter the request sequence (space-separated): ").split()))
initial_head = int(input("Enter the initial head position: "))

head_path = [initial_head] + requests

total_movement = 0
current_position = initial_head

for track in requests:
    total_movement += abs(track - current_position)
    current_position = track

print("\n--- FCFS Disk Scheduling ---")
print("Head Movement Path:", " -> ".join(map(str, head_path)))
print("Total Head Movement (Seek Operations):", total_movement, "tracks")
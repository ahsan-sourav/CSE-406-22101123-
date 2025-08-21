# LAB 7 | SCAN Disk Scheduling (direction = left) algorithm

requests = list(map(int, input("Enter request sequence (space-separated): ").split()))
head = int(input("Enter the initial head position: "))
requests.sort()

seek_count = 0
accessed_tracks = []

left = [track for track in requests if track <= head]
right = [track for track in requests if track > head]

for track in reversed(left):
    seek_count += abs(head - track)
    head = track
    accessed_tracks.append(track)

for track in right:
    seek_count += abs(head - track)
    head = track
    accessed_tracks.append(track)

# Output the results
print("Accessed track sequence:", accessed_tracks)
print("Total seek time:", seek_count)
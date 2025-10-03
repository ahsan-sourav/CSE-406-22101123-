# LAB 9 | FIFO Page Replacement Algorithm

f = int(input("Enter number of frames: "))
n = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter pages (space separated): ").split()))
frames = []
faults = 0
for p in pages:
    if p not in frames:
        if len(frames) < f:
            frames.append(p)
        else:
            frames.pop(0)
            frames.append(p)
        faults += 1
print("Total Page Faults:", faults)
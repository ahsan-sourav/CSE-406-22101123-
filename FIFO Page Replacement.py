# LAB 9 | FIFO Page Replacement Algorithm

num_frames = int(input("Enter number of frames: "))
num_pages = int(input("Enter number of pages: "))
pages = list(map(int, input("Enter page reference string (space separated): ").split()))

frames = []
page_faults = 0

for page in pages:
    if page not in frames:
        if len(frames) < num_frames:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)
        page_faults += 1
        
print("\nTotal Page Faults:", page_faults)
# LAB 10 | LRU Page Replacement

def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0

    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)
            frames.append(page)
        print(f"Page: {page} -> Frames: {frames}")

    print("\nTotal Page Faults:", page_faults)


# Take user input
pages = list(map(int, input("Enter pages (space separated): ").split()))
frame_size = int(input("Enter frame size: "))

lru_page_replacement(pages, frame_size)

# LAB 2 | Shortest Job First Algorithm

def sjf_scheduling():
    num = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num):
        pid = input(f"Enter PID for process {i + 1}: ")
        arrival = int(input(f"Enter Arrival Time for {pid}: "))
        burst = int(input(f"Enter Burst Time for {pid}: "))
        processes.append({
            'PID': pid,
            'AT': arrival,
            'BT': burst
        })

    # Sort by arrival time initially
    processes.sort(key=lambda x: (x['AT'],x['BT']))
    
    time = 0
    completed = 0
    ready_queue = []
    executed = []

    while completed < num:
        for p in processes:
            if p not in ready_queue and p not in executed and p['AT'] <= time:
                ready_queue.append(p)
        if not ready_queue:
            time += 1
            continue

        ready_queue.sort(key=lambda x: x['BT'])
        current = ready_queue.pop(0)

        start_time = time
        completion_time = time + current['BT']
        turnaround_time = completion_time - current['AT']
        waiting_time = turnaround_time - current['BT']

        current.update({
            'Completion': completion_time,
            'Turnaround': turnaround_time,
            'Waiting': waiting_time
        })

        executed.append(current)
        time = completion_time
        completed += 1

    print("\nSJF Scheduling Result: ")
    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("PID", "AT", "BT", "CT", "TAT", "WT"))

    total_WT = 0
    total_TAT = 0

    for p in executed:
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(p['PID'],p['AT'],p['BT'],p['Completion'],p['Turnaround'],p['Waiting']))
        total_WT += p['Waiting']
        total_TAT += p['Turnaround']

    avg_WT = total_WT/num
    avg_TAT = total_TAT/num

    print(f"\nAverage Waiting Time: {avg_WT:.2f}")
    print(f"Average Turnaround Time: {avg_TAT:.2f}")

sjf_scheduling()
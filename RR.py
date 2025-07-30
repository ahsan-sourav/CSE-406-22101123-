# LAB 3 | Round Robin CPU Scheduling

def round_robin_scheduling():
    num = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num):
        pid = input(f"Enter PID for process {i+1}: ")
        at = int(input(f"Enter Arrival Time for {pid}: "))
        bt = int(input(f"Enter Burst Time for {pid}: "))
        processes.append({
            'PID': pid,
            'AT': at,
            'BT': bt,
            'RT': bt,   # remaining time
            'CT': 0,
            'TAT': 0,
            'WT': 0
        })

    tq = int(input("Enter Time Quantum: "))
    time = 0
    queue = []
    completed = 0
    visited = [False] * num

    print("\nRound Robin Scheduling Result:")
    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("PID", "AT", "BT", "CT", "TAT", "WT"))

    while completed < num:
        for i in range(num):
            if processes[i]['AT'] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not queue:
            time += 1
            continue

        index = queue.pop(0)
        exec_time = min(tq, processes[index]['RT'])
        time += exec_time
        processes[index]['RT'] -= exec_time

        # check if new processes arrived during execution
        for i in range(num):
            if processes[i]['AT'] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if processes[index]['RT'] == 0:
            processes[index]['CT'] = time
            processes[index]['TAT'] = time - processes[index]['AT']
            processes[index]['WT'] = processes[index]['TAT'] - processes[index]['BT']
            completed += 1
        else:
            queue.append(index)

    total_TAT = 0
    total_WT = 0

    for p in processes:
        total_TAT += p['TAT']
        total_WT += p['WT']
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(p['PID'], p['AT'], p['BT'], p['CT'], p['TAT'], p['WT']))

    avg_TAT = total_TAT / num
    avg_WT = total_WT / num

    print("\nAverage Turn Around Time: {:.2f}".format(avg_TAT))
    print("Average Waiting Time: {:.2f}".format(avg_WT))
    
round_robin_scheduling()

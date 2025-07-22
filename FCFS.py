
# LAB 1 | FCFS CPU Scheduling

def fcfs_scheduling():
    num = int(input("Enter the number of processes: "))
    processes = []  # dictunaries for holding process

    # Taking input and arranging them in order
    for i in range(num):
        pid = input(f"Enter PID for process {i+1}: ")
        arrival_time = int(input(f"Enter Arrival Time for {pid}: "))
        brust_time = int(input(f"Enter Brust Time for {pid}: "))
        processes.append({
            'PID' : pid,
            'AT' : arrival_time,
            'BT' : brust_time
        })

    processes.sort(key=lambda x: x['AT'])

    current_time = 0
    total_WT = 0    # wating time
    total_TAT = 0   # trun aroud time

    print("\nFCFS Scheduling Result: ")
    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("PID","AT","BT","CT","TAT","WT"))

    for process in processes:
        at = process['AT']
        bt = process['BT']

        # Idel CPU
        if current_time < at:
            current_time = at

        # Calculation
        ct = current_time+bt
        process['CT'] = ct
        process['TAT'] = ct-at
        process['WT'] = process['TAT']-bt

        total_TAT += process['TAT']
        total_WT += process['WT']
        current_time = ct

        # Print Calcution
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(process['PID'],at,bt,process['CT'],process['TAT'],process['WT']))


    avg_WT = total_WT/num
    avg_TAT = total_TAT/num

    print("\nAverage Waiting Time : {:.2f}".format(avg_WT))
    print("Average Turn Around Time: {:.2f}".format(avg_TAT))

fcfs_scheduling()
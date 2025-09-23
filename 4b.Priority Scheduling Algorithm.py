def priorityScheduling(processes):
    # Sort by priority (highest first)
    processes.sort(key=lambda x: x[2], reverse=True)

    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Waiting time calculation
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

    # Turnaround time calculation
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

    # Print table
    print("Process\tBurst\tPriority\tWaiting\tTurnaround")
    total_wt, total_tat = 0, 0
    for i in range(n):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"P{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t\t{waiting_time[i]}\t{turnaround_time[i]}")

    # Averages
    print("\nAverage Waiting Time:", total_wt/n)
    print("Average Turnaround Time:", total_tat/n)


# Example
processes = [[1, 10, 1], [2, 5, 0], [3, 8, 1]]
priorityScheduling(processes)

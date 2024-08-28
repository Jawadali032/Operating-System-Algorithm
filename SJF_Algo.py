def main():
    # Taking the number of processes
    n = int(input("Enter number of processes: "))

    # Matrix for storing Process Id, Arrival Time, Burst Time, Waiting Time & Turnaround Time.
    A = [[0 for j in range(5)] for i in range(n)]
    total_wt, total_tat = 0, 0
    gantt_chart = []

    print("Enter Arrival Time and Burst Time:")
    for i in range(n):
        A[i][0] = int(input(f"P{i + 1} Arrival Time: "))
        A[i][2] = int(input(f"P{i + 1} Burst Time: "))
        A[i][1] = i + 1  # Process ID

    # Sorting processes based on Arrival Time and then Burst Time
    A.sort(key=lambda x: (x[0], x[2]))

    A[0][3] = 0  # Waiting Time for the first process
    A[0][4] = A[0][2]  # Turnaround Time for the first process

    for i in range(1, n):
        A[i][3] = max(0, A[i - 1][4] - A[i][0])  # Waiting Time
        A[i][4] = A[i][3] + A[i][2]  # Turnaround Time

    # Calculate total waiting time and total turnaround time
    for i in range(n):
        total_wt += A[i][3]
        total_tat += A[i][4]

    avg_wt = total_wt / n
    avg_tat = total_tat / n

    # Printing the table
    print("P\tAT\tE_T\tWT\tTAT")
    for i in range(n):
        print(f"P{A[i][1]}\t{A[i][0]}\t{A[i][2]}\t{A[i][3]}\t{A[i][4]}")

    # Printing the Gantt Chart
    print("\nGantt Chart:")
    for i in range(n):
        process_id = A[i][1]
        gantt_chart.extend([f"P{process_id}"] * A[i][2])
    print(" || ".join(gantt_chart))

    print(f"Average Waiting Time= {avg_wt}")
    print(f"Average Turnaround Time= {avg_tat}")


if __name__ == "__main__":
    main()

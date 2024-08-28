# Function to find the waiting time
# for all processes
def findWaitingTime(processes, n, wt):
    rt = [0] * n
 
    # Copy the burst time into rt[]
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
 
    # Process until all processes gets
    # completed
    while (complete != n):
         
        # Find process with minimum remaining
        # time among the processes that
        # arrives till the current time`
        for j in range(n):
            if ((processes[j][2] <= t) and
                (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
               
        if (check == False):
            t += 1
            continue   
        # Reduce remaining time by one
        rt[short] -= 1
 
        # Update minimum
        minm = rt[short]
        
        # Gant_Chart=[]
        value = short+1
        # Gant_Chart.append(value)
        print("[","P",value,"]", "at t = ", t+1)
        # print("P",value)
        
        if (minm == 0):
            minm = 999999999
 
        # If a process gets completely
        # executed
        if (rt[short] == 0):
 
            # Increment complete
            complete += 1
            check = False
 
            # Find finish time of current
            # process
            fint = t + 1
 
            # Calculate waiting time
            wt[short] = (fint - proc[short][1] -   
                                proc[short][2])
 
            if (wt[short] < 0):
                wt[short] = 0
                        
        # Increment time
        t += 1
    
        
# Function to calculate turn around time
def findTurnAroundTime(processes, n, wt, tat):
     
    # Calculating turnaround time
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]
 
# Function to calculate average waiting
# and turn-around times.
          
def findavgTime(processes, n):
    wt = [0] * n
    tat = [0] * n
    exe_T= [0] * n
    # Function to find waiting time
    # of all processes
    print("GANT CHART")
    findWaitingTime(processes, n, wt)
 
    # Function to find turn around time
    # for all processes
    findTurnAroundTime(processes, n, wt, tat)
 
    # Display processes along with all details
    print("| Processes      | Execution Time|    Arrivals   |  Waiting",
                    "Time | Turn-Around Time|")
    total_wt = 0
    total_tat = 0
    total_Exe_T = 0
    
    for i in range(n):
        
        exe_T[i]= processes[i][1]
        
    for i in range(n):
 
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        total_Exe_T = total_Exe_T + exe_T[i]
        print("|",processes[i][0], "\t\t","|",
                   processes[i][1], "\t\t","|",
                   processes[i][2], "\t\t","|",
                   wt[i], "\t\t","|", tat[i],"\t\t","  |")
        
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = ", total_tat / n)
    print("Server Utilization = ", total_Exe_T / total_tat)
         
# # Driver code
# if __name__ =="__main__":
     
#     # Process id's
    
#     proc = [[1, 10, 0], [2, 1, 1],
#             [3, 2, 2], [4, 1, 3], [5,5,4]]
#     n = 5
#     findavgTime(proc, n)

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    
    proc = []
    for i in range(n):
        process_id = i + 1
        burst_time = int(input(f"Enter execution time for process {process_id}: "))
        arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
        proc.append([process_id, burst_time, arrival_time])
    
    findavgTime(proc, n)

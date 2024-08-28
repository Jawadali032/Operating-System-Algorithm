#  program for Highest Response Ratio
# (HRRN) Scheduling
 
# Function to sort process by arrival time
def sortByArrival(at, n):
     
    # Selection Sort applied 
    for i in range(0, n - 1):
        for j in range(i + 1, n):
             
            # Check for lesser arrival time 
            if at[i] > at[j]:
                 
                # Swap earlier process to front
                at[i], at[j] = at[j], at[i]
 
# Driver code
if __name__ == '__main__':
     
    sum_bt = 0
    avgwt = 0
    avgTT = 0
    n = 5
     
    completed =[0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    normalised_TT = [0] * n
     
    # Predefined arrival times 
    arrival_time = [ 0, 2, 4, 6, 8 ]
     
    # Predefined burst times 
    burst_time = [ 3, 6, 4, 5, 2 ]
    process = []
     
    # Initializing the structure variables 
    for i in range(0, n):
        process.append(chr(65 + i))
        sum_bt += burst_time[i]
         
    # Sorting the structure by arrival times 
    sortByArrival(arrival_time, n)
    print("Name   ",    "   Arrival time  ",
          "Burst time   ", "Waiting Time    ",
          "Turnaround Time ", "    Normalized TT")
    t = arrival_time[0]
     
    while(t < sum_bt):
         
        # Set lower limit to response ratio 
        hrr = -9999
        temp, loc = 0, 0
         
        for i in range(0, n):
             
            # Checking if process has arrived
            # and is Incomplete 
            if arrival_time[i] <= t and completed[i] != 1:
                 
                # Calculating Response Ratio 
                temp = ((burst_time[i] +
                        (t - arrival_time[i])) /
                         burst_time[i])
                          
                # Checking for Highest Response Ratio 
                if hrr < temp:
                     
                    # Storing Response Ratio 
                    hrr = temp
                     
                    # Storing Location
                    loc = i
                     
        # Updating time value 
        t += burst_time[loc]
         
        # Calculation of waiting time
        waiting_time[loc] = (t - arrival_time[loc] -
                                 burst_time[loc])
         
        # Calculation of Turn Around Time 
        turnaround_time[loc] = t - arrival_time[loc]
         
        # Sum Turn Around Time for average 
        avgTT += turnaround_time[loc]
         
        # Calculation of Normalized Turn Around Time 
        normalised_TT = float(turnaround_time[loc] /
                              burst_time[loc])
         
        # Updating Completion Status
        completed[loc] = 1
         
        # Sum Waiting Time for average 
        avgwt += waiting_time[loc]
         
        print(process[loc], "\t\t", arrival_time[loc],
              "\t\t", burst_time[loc], "\t\t",
              waiting_time[loc], "\t\t",
              turnaround_time[loc], "\t\t",
              "{0:.6f}".format(normalised_TT))
 
    print("Average waiting time: {0:.6f}".format(avgwt / n))
    print("Average Turn Around time:  {0:.6f}".format(avgTT / n))
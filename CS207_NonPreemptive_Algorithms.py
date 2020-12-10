import math
import numpy as np

completion_time = []
turnaround_time = []
waiting_time = []
processes = []

def FCFS_time(num_processes, arrival_time, burst_time): 
    burst_time_sorted = []
    waiting_time_sorted = []
    turnaround_time_sorted = []
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
        burst_time_sorted.append(0)
        waiting_time_sorted.append(0)
        turnaround_time_sorted.append(0)
    
    idx_list_sorted = np.argsort(arrival_time)
    for idx, sorted_idx in enumerate(idx_list_sorted):
        burst_time_sorted[idx] = burst_time[sorted_idx]

    waiting_time[i] = 0
    for i in range(1, num_processes):
        waiting_time[i] = burst_time_sorted[i-1] + waiting_time[i-1]
    
    for i, j in enumerate(idx_list_sorted):
        waiting_time_sorted[j] = waiting_time[i]

    for i in range(num_processes):
        turnaround_time[i] = burst_time_sorted[i] + waiting_time[i]
    
    for i, j in enumerate(idx_list_sorted):
        turnaround_time_sorted[j] = turnaround_time[i]
    
    print(waiting_time_sorted)
    print(turnaround_time_sorted)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))

def SJF_time(num_processes, arrival_time, burst_time):  
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)

    for i in range(num_processes):
        for j in range(num_processes):
            if arrival_time[i] < arrival_time[j]:
                temp = arrival_time[j]
                arrival_time[j] = arrival_time[i]
                arrival_time[i] = temp
                temp = burst_time[j]
                burst_time[j] = burst_time[i]
                burst_time[i] = temp
    
    for i in range(num_processes):
        pos = i
        limit = i+1
        for j in range(limit, num_processes):
            if burst_time[j] < burst_time[pos]:
                pos = j
        
        temp = burst_time[i]
        burst_time[i] = burst_time[pos]
        burst_time[pos] = temp

    waiting_time[0] = 0
    for i in range(num_processes):
        waiting_time[i] = 0
        for j in range(i):
            waiting_time[i] += burst_time[j]
    
    for i in range(num_processes):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print(waiting_time)
    print(turnaround_time)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))

def Prio_time(num_processes, arrival_time, burst_time, priority):  
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)

    for i in range(num_processes):
        limit = num_processes-i-1
        for j in range(limit):
            if arrival_time[j] > arrival_time[j+1]: #check arrival time first
                temp = arrival_time[j]
                arrival_time[j] = arrival_time[j+1]
                arrival_time[j+1] = temp
                
                temp = burst_time[j]
                burst_time[j] = burst_time[j+1]
                burst_time[j+1] = temp

                temp = priority[j]
                priority[j] = priority[j+1]
                priority[j+1] = temp

            if priority[j] > priority[j+1]: #check priority
                temp = arrival_time[j]
                arrival_time[j] = arrival_time[j+1]
                arrival_time[j+1] = temp
                
                temp = burst_time[j]
                burst_time[j] = burst_time[j+1]
                burst_time[j+1] = temp

                temp = priority[j]
                priority[j] = priority[j+1]
                priority[j+1] = temp

    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    for i in range(1, num_processes):
        completion_time[i] = burst_time[i] + completion_time[i-1]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    print(completion_time)
    print(waiting_time)
    print(turnaround_time)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))



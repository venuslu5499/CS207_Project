import math
import numpy as np

completion_time = []
turnaround_time = []
waiting_time = []

completion_time_resorted = []
waiting_time_resorted = []
turnaround_time_resorted = []

def clear_list(completion_time, turnaround_time, waiting_time):
    completion_time.clear()
    turnaround_time.clear()
    waiting_time.clear()

def FCFS_time(num_processes, arrival_time, burst_time): 
    idx = []
    idx = arrival_time.copy()

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

    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    for i in range(1, num_processes):
        completion_time[i] = burst_time[i] + completion_time[i-1]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    for i in range(num_processes):
        for j in range(num_processes):
            if idx[i] == arrival_time[j]:
                completion_time_resorted.append(completion_time[j])
                waiting_time_resorted.append(waiting_time[j])
                turnaround_time_resorted.append(turnaround_time[j])
                arrival_time[j] = -9999

    print(completion_time_resorted)
    print(waiting_time_resorted)
    print(turnaround_time_resorted)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))
    clear_list(completion_time, turnaround_time, waiting_time)

def SJF_time(num_processes, arrival_time, burst_time):  
    idx = []
    idx = burst_time.copy()
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
    burst_time.append(0) # to avoid error: list index out of range

    for i in range(num_processes): 
        for j in range(num_processes):
            if arrival_time[i] < arrival_time[j]:
                temp = arrival_time[j]
                arrival_time[j] = arrival_time[i]
                arrival_time[i] = temp
                temp = burst_time[j]
                burst_time[j] = burst_time[i]
                burst_time[i] = temp
    
    result = all(elem == arrival_time[0] for elem in arrival_time)
    
    if result == False:
        bt = 0
        k = 1
        for j in range(num_processes):
            bt = bt + burst_time[j]
            minimum = burst_time[k]
            for i in range(k, num_processes):
                if bt >= arrival_time[i] and burst_time[i] < minimum:
                    temp = arrival_time[k]
                    arrival_time[k] = arrival_time[i]
                    arrival_time[i] = temp
                    temp = burst_time[k]
                    burst_time[k] = burst_time[i]
                    burst_time[i] = temp
            k=+1
    elif result == True:
        limit = num_processes-1
        for i in range(limit):
            for j in range(limit):
                if burst_time[j] > burst_time[j+1]:
                    temp = arrival_time[j]
                    arrival_time[j] = arrival_time[j+1]
                    arrival_time[j+1] = temp
                    temp = burst_time[j]
                    burst_time[j] = burst_time[j+1]
                    burst_time[j+1] = temp

    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    for i in range(1, num_processes):
        completion_time[i] = burst_time[i] + completion_time[i-1]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    for i in range(num_processes):
        for j in range(num_processes):
            if idx[i] == burst_time[j]:
                completion_time_resorted.append(completion_time[j])
                waiting_time_resorted.append(waiting_time[j])
                turnaround_time_resorted.append(turnaround_time[j])
                arrival_time[j] = -9999

    print(completion_time_resorted)
    print(waiting_time_resorted)
    print(turnaround_time_resorted)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))
    clear_list(completion_time, turnaround_time, waiting_time)

def Prio_time(num_processes, arrival_time, burst_time, priority):  
    idx = []
    idx = arrival_time.copy()
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)

    for i in range(num_processes):
        limit = num_processes-i-1
        for j in range(limit):
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

    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    for i in range(1, num_processes):
        completion_time[i] = burst_time[i] + completion_time[i-1]
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    for i in range(num_processes):
        for j in range(num_processes):
            if idx[i] == arrival_time[j]:
                completion_time_resorted.append(completion_time[j])
                waiting_time_resorted.append(waiting_time[j])
                turnaround_time_resorted.append(turnaround_time[j])
                arrival_time[j] = -9999

    print(completion_time_resorted)
    print(waiting_time_resorted)
    print(turnaround_time_resorted)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))
    clear_list(completion_time, turnaround_time, waiting_time)



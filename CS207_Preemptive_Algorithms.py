import math
import CS207_NonPreemptive_Algorithms as nonpre

completion_time = []
turnaround_time = []
waiting_time = []
processes = []

def clear_list(completion_time, turnaround_time, waiting_time, processes):
    completion_time.clear()
    turnaround_time.clear()
    waiting_time.clear()
    processes.clear()

def SRTF_time(num_processes, arrival_time, burst_time): 
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
        processes.append(0)

    smallest = 0
    count = 0
    end = 0
    time = 0

    for i in range(0, num_processes):
        processes[i] = burst_time[i]
    burst_time.append(9999)

    while count != num_processes:
        smallest = -1
        for i in range(num_processes):
            if arrival_time[i] <= time and burst_time[i] < burst_time[smallest] and burst_time[i] > 0:
                smallest = i
        burst_time[smallest] = burst_time[smallest] - 1

        if burst_time[smallest] == 0:
            count = count + 1
            end = time + 1
            completion_time[smallest] = end
            waiting_time[smallest] = end - arrival_time[smallest] - processes[smallest]
            turnaround_time[smallest] = end - arrival_time[smallest]
        time = time + 1

    print("\nWaiting Time \t Turnaround Time")
    for i in range(0, num_processes):
        print(str(waiting_time[i]) + "\t\t\t" + str(turnaround_time[i]))
    print("Average Waiting Time: ", sum(waiting_time)/len(waiting_time))
    print("Average Turnaround Time: ", sum(turnaround_time)/len(turnaround_time))
    clear_list(completion_time, turnaround_time, waiting_time, processes)

def RR_time(num_processes, arrival_time, burst_time, quantum): 
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
    
    remain_time = burst_time.copy()
    remain_process = num_processes

    flag = 0
    exec_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    i = 0
    while remain_process !=0:
        if remain_time[i] <= quantum and remain_time[i] > 0:
            exec_time += remain_time[i]
            remain_time[i] = 0
            flag = 1
        elif remain_time[i] > 0:
            remain_time[i] -= quantum
            exec_time += quantum
        
        if flag == 1 and remain_time[i] == 0:

            turnaround_time[i] = exec_time - arrival_time[i]
            waiting_time[i] = turnaround_time[i] - burst_time[i]
            total_waiting_time += waiting_time[i]
            total_turnaround_time += turnaround_time[i]
            flag = 0
            remain_process -= 1
        
        if i == num_processes - 1:
            i = 0
        elif arrival_time[i+1] <= exec_time:
            i += 1
        else:
            i = 0

    print("\nWaiting Time \t Turnaround Time")
    for i in range(0, num_processes):
        print(str(waiting_time[i]) + "\t\t\t" + str(turnaround_time[i]))
    print("Average Waiting Time: ", (total_waiting_time/num_processes))
    print("Average Turnaround Time: ", (total_turnaround_time/num_processes))
    clear_list(completion_time, turnaround_time, waiting_time, processes)

def P_Prio_time(num_processes, arrival_time, burst_time, priority):
    completion_time = []
    turnaround_time = []
    waiting_time = []  
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
        processes.append(0)

    for i in range(num_processes):
        processes[i] = burst_time[i]

    priority.append(-1)
    count = 0
    time = 0
    while count != num_processes:
        smallest = num_processes
        for i in range(num_processes):
            if arrival_time[i] <= time and priority[i] > priority[smallest] and burst_time[i] > 0:
                smallest = i
        burst_time[smallest] = burst_time[smallest] - 1

        if burst_time[smallest] == 0:
            count = count + 1
            end = time + 1
            completion_time[smallest] = end
            waiting_time[smallest] = end - arrival_time[smallest] - processes[smallest]
            turnaround_time[smallest] = end - arrival_time[smallest]
        
        time = time + 1
            
    print("\nWaiting Time \t Turnaround Time")
    for i in range(0, num_processes):
        print(str(waiting_time[i]) + "\t\t\t" + str(turnaround_time[i]))
    print("Average Waiting Time: ", sum(waiting_time)/len(waiting_time))
    print("Average Turnaround Time: ", sum(turnaround_time)/len(turnaround_time))
    clear_list(completion_time, turnaround_time, waiting_time, processes)


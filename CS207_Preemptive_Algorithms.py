import math

completion_time = []
turnaround_time = []
waiting_time = []
processes = []

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

    for i in range(num_processes):
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
    print(completion_time)
    print(waiting_time)
    print(turnaround_time)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))

def RR_time(num_processes, arrival_time, burst_time, quantum): 
    for i in range(num_processes):
        completion_time.append(0)
        turnaround_time.append(0)
        waiting_time.append(0)
        processes.append(0)

    smallest = 0
    count = 0
    end = 0
    time = 0

    for i in range(num_processes):
        processes[i] = burst_time[i]
    burst_time.append(9999)

    while count != num_processes:
        smallest = -1
        for i in range(num_processes):
            if arrival_time[i] <= time and burst_time[i] < burst_time[smallest] and burst_time[i] > 0:
                smallest = i
        burst_time[smallest] = burst_time[smallest] - 1

        if burst_time[smallest] > quantum:
            time = time + quantum
            burst_time[smallest] = burst_time[smallest] - quantum
        time = time + burst_time[smallest]
        count = count + 1
        end = time + 1
        completion_time[smallest] = end
        waiting_time[smallest] = end - arrival_time[smallest] - processes[smallest]
        turnaround_time[smallest] = end - arrival_time[smallest]
    print(completion_time)
    print(waiting_time)
    print(turnaround_time)
    print(sum(waiting_time)/len(waiting_time))
    print(sum(turnaround_time)/len(turnaround_time))


def P_Prio_time():  
    #Andrea
    pass



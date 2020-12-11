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
            total_waiting_time += exec_time - arrival_time[i] - burst_time[i]
            total_turnaround_time += exec_time - arrival_time[i]
            flag = 0
            remain_process -= 1
        
        if i == num_processes - 1:
            i = 0
        
        elif arrival_time[i+1] <= exec_time:
            i += 1
        
        else:
            i = 0

    print("Average Waiting Time: ", (total_waiting_time/num_processes))
    print("Average Turnaround Time: ", (total_turnaround_time/num_processes))

    # smallest = 0
    # count = 0
    # end = 0
    # time = 0

    # for i in range(num_processes):
    #     processes[i] = burst_time[i]
    # burst_time.append(9999)

    # while count != num_processes:
    #     smallest = -1
    #     for i in range(num_processes):
    #         if arrival_time[i] <= time and burst_time[i] < burst_time[smallest] and burst_time[i] > 0:
    #             smallest = i
    #     burst_time[smallest] = burst_time[smallest] - 1

    #     if burst_time[smallest] > quantum:
    #         time = time + quantum
    #         burst_time[smallest] = burst_time[smallest] - quantum
    #     time = time + burst_time[smallest]
    #     count = count + 1
    #     end = time + 1
    #     completion_time[smallest] = end
    #     waiting_time[smallest] = end - arrival_time[smallest] - processes[smallest]
    #     turnaround_time[smallest] = end - arrival_time[smallest]
        
    # print(completion_time)
    # print(waiting_time)
    # print(turnaround_time)
    # print(sum(waiting_time)/len(waiting_time))
    # print(sum(turnaround_time)/len(turnaround_time))


def P_Prio_time():  
    #Alex / Andrea / Matthew
    pass
import math
import CS207_Preemptive_Algorithms as pre
import CS207_NonPreemptive_Algorithms as nonpre

def input_arrival_time(num_process):
    arrival_time = []
    print("Input Individual Arrival Time")
    for i in range(1, num_process+1):
        time = input("AT" +str(i) +": ")
        arrival_time.append(int(time))
    return arrival_time

def input_burst_time(num_process):
    burst_time = []
    print("Input Individual Burst Time")
    for i in range(1, num_process+1):
        time = input("BT" +str(i) +": ")
        burst_time.append(int(time))
    return burst_time

def input_priority_number(num_process):
    priority_num = []
    print("Input Individual Priority Number")
    for i in range(1, num_process+1):
        priority = input("Prio" +str(i) +": ")
        priority_num.append(int(priority))
    return priority_num

def input_scheduling_algorithm():
    print("Input Individual Burst Time")
    print("CPU Scheduling Algorithm: \n"
        +"[A] Shortest Remaining Time First (SRTF) \n"
        +"[B] First Come First Serve (FCFS) \n"
        +"[C] Priority (Non-Preemptive) \n"
        +"[D] Shortest Job First (SJF) \n"
        +"[E] Round Robin (RR) \n"
        +"[F] Exit ")
    algorithm = input("Enter Choice: ")
    return algorithm

program = True
while program == True:
    num_process = int(input("Input no. of Processes [2-9]: "))
    if num_process < 2 or num_process > 9:
        print("Must be a number between 2-9")
    else:
        arrival_time = input_arrival_time(num_process)
        burst_time = input_burst_time(num_process)
        algorithm = input_scheduling_algorithm()

        if algorithm == "A":
            pre.SRTF_time(num_process, arrival_time, burst_time)

        elif algorithm == "B":
            nonpre.FCFS_time(num_process, arrival_time, burst_time)
        
        elif algorithm == "C":
            priority = input_priority_number(num_process)
            nonpre.Prio_time(num_process, arrival_time, burst_time, priority)
        
        elif algorithm == "D":
            nonpre.SJF_time(num_process, arrival_time, burst_time)

        elif algorithm == "E":
            quantum = int(input("Input time slice: "))
            pre.RR_time(num_process, arrival_time, burst_time, quantum)

        elif algorithm == "F":
            again = input("Input Again (y/n)? ")
            if again == "y":
                continue
            elif again == "n":
                break
    




import math
import CS207_Preemptive_Algorithms as pre
import CS207_NonPreemptive_Algorithms as nonpre
import CS207_DiskSched_Algorithms as disk


def input_arrival_time(num_process):
    arrival_time = []
    print("Input Individual Arrival Time")
    for i in range(1, num_process+1):
        time = input("AT" + str(i) + ": ")
        arrival_time.append(int(time))
    return arrival_time


def input_burst_time(num_process):
    burst_time = []
    print("Input Individual Burst Time")
    for i in range(1, num_process+1):
        time = input("BT" + str(i) + ": ")
        burst_time.append(int(time))
    return burst_time


def input_priority_number(num_process):
    priority_num = []
    print("Input Individual Priority Number")
    for i in range(1, num_process+1):
        priority = input("Prio" + str(i) + ": ")
        priority_num.append(int(priority))
    return priority_num


def input_pre_scheduling_algorithm():
    print("Input Individual Burst Time")
    print("CPU Scheduling Algorithm: \n"
        +"[A] Shortest Remaining Time First (SRTF) \n"
        +"[B] Round Robin (RR) \n"
        +"[C] Priority (P-Prio) \n"
        +"[D] Exit")
    algorithm = input("Enter Choice: ")
    return algorithm

def input_nonpre_scheduling_algorithm():
    print("Input Individual Burst Time")
    print("CPU Scheduling Algorithm: \n"
        +"[A] First Come First Serve (FCFS) \n"
        +"[B] Shortest Job First (SJF) \n"
        +"[C] Priority (Prio) \n"
        +"[D] Exit")
    algorithm = input("Enter Choice: ")
    return algorithm


def input_request_sequence(num_request):
    request_sequence = []
    for i in range(1, num_request+1):
        location = input("Loc "+str(i)+": ")
        request_sequence.append(int(location))
    return request_sequence


def input_disk_scheduling_algorithm():
    print("Disk Scheduling Algorithm: \n"
          + "[A] First Come First Serve (FCFS) \n"
          + "[B] Shortest Seek Time First (SSTF) \n"
          + "[C] Scan \n"
          + "[D] Look \n"
          + "[E] Circular Scan (CSCAN) \n"
          + "[F] Circular Look (CLOOK) \n"
          + "[G] Exit ")
    disk_sched_algorithm = input("Enter Choice: ")
    return disk_sched_algorithm

program = True
while program == True:
    scheduling = input("\nChoose Scheduling Type: \n" #Choose the scheduling type
                        + "[1] CPU Scheduling \n"
                        + "[2] Disk Scheduling \n"
                        + "Input: ")

    if scheduling == "1":
        cpu_scheduling = input("Choose CPU Scheduling Type: \n"  #Choose the cpu scheduling type
                                + "[1] Preemptive \n"
                                + "[2] Non-Preemptive \n"
                                + "Input: ")
        num_process = int(input("Input no. of Processes [2-9]: "))
        if num_process < 2 or num_process > 9:
            print("Must be a number between 2-9")
        else:
            if cpu_scheduling == "1":
                arrival_time = input_arrival_time(num_process)
                burst_time = input_burst_time(num_process)
                algorithm = input_pre_scheduling_algorithm()  #Choose the preemptive cpu scheduling type
           
                if algorithm == "A":
                    pre.SRTF_time(num_process, arrival_time, burst_time)

                elif algorithm == "B":
                    quantum = int(input("Input time slice: "))
                    pre.RR_time(num_process, arrival_time, burst_time, quantum)

                elif algorithm == "C":
                    priority = input_priority_number(num_process)
                    pre.P_Prio_time(num_process, arrival_time, burst_time, priority)
                
                elif algorithm == "D":
                    again = input("Input Again (y/n)? ")
                    if again == "y":
                        continue
                    elif again == "n":
                        break

            elif cpu_scheduling == "2":
                arrival_time = input_arrival_time(num_process)
                burst_time = input_burst_time(num_process)
                algorithm = input_nonpre_scheduling_algorithm() #Choose the non preemptive cpu scheduling type

                if algorithm == "A":
                    nonpre.FCFS_time(num_process, arrival_time, burst_time)
                
                elif algorithm == "B":
                    nonpre.SJF_time(num_process, arrival_time, burst_time)

                elif algorithm == "C":
                    priority = input_priority_number(num_process)
                    nonpre.Prio_time(num_process, arrival_time, burst_time, priority)

                elif algorithm == "D":
                    again = input("Input Again (y/n)? ")
                    if again == "y":
                        continue
                    elif again == "n":
                        break

    elif scheduling == "2":
        current_position = int(input("Input current position: "))
        track_size = int(input("Input track size: "))
        seek_rate = int(input("Input seek rate: "))
        num_request = int(input("Input number of request [max of 10]: "))

        if num_request > 10:
            print("The program will only be accepting a maximum of 10 requests.")
        else:
            request_sequence = input_request_sequence(num_request)
            disk_algo = input_disk_scheduling_algorithm()  #Choose the disk scheduling type
            if disk_algo == "A":
                disk.FCFS_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "B":
                disk.SSTF_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "C":
                disk.Scan_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "D":
                disk.Look_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "E":
                disk.CScan_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "F":
                disk.CLook_time(current_position, track_size, seek_rate, request_sequence)

            elif disk_algo == "G":
                again = input("Input Again (y/n)? ")
                if again == "y":
                    continue
                elif again == "n":
                    break

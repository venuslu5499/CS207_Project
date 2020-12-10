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


def input_request_sequence(num_request):
    request_sequence = []
    for i in range(1, num_request+1):
        location = input("Loc1"+str(i)+": ")
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

# suggested flow
program = True
while program == True:
    scheduling = input("Choose scheduling type: \n"
                       + "[1] CPU Scheduling \n"
                        + "[2] Disk Scheduling \n")
    if scheduling == "1":
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
                nonpre.Prio_time(num_process, arrival_time,
                                 burst_time, priority)

            elif algorithm == "D":
                nonpre.SJF_time(num_process, arrival_time, burst_time)

            elif algorithm == "E":
                again = input("Input Again (y/n)? ")
                if again == "y":
                    continue
                elif again == "n":
                    break
    elif scheduling == "2":
        current_position = int(input("Input current position:"))
        track_size = int(input("Input track size: "))
        seek_rate = int(input("Input seek rate: "))
        num_request = int(input("Input number of request [max of 10]: "))
       
        if num_request > 10:
            print("The program will only be accepting a maximum of 10 requests.")
        else:
            request_sequence = input_request_sequence(num_request)
            disk_algo = input_disk_scheduling_algorithm()
            if disk_algo == "A":
                disk.FCFS_time(current_position, track_size,
                               seek_rate, request_sequence)
            elif disk_algo == "B":
                disk.SSTF_time(current_position, track_size,
                               seek_rate, request_sequence)
            elif disk_algo == "C":
                disk.Scan_time(current_position, track_size,
                               seek_rate, request_sequence)
            elif disk_algo == "D":
                disk.Look_time(current_position, track_size,
                               seek_rate, request_sequence)
            elif disk_algo == "E":
                disk.CScan_time(current_position, track_size,
                                seek_rate, request_sequence)
            elif disk_algo == "F":
                disk.CLook_time(current_position, track_size,
                                seek_rate, request_sequence)
            elif disk_algo == "G":
                again = input("Input Again (y/n)? ")
                if again == "y":
                    continue
                elif again == "n":
                    break

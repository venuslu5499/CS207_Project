import math

completion_time = []
turnaround_time = []
waiting_time = []
processes = []

def FCFS_time(num_requests, current_position, request_locations):
    seek_count = 0
    distance, current_track = 0, 0
    head_movement = []

    for i in range(num_requests):
        current_track = request_locations[i] 
        distance = abs(current_track - current_position);
        head_movement.append(abs(current_position - current_track))
        seek_count += distance
        current_position = current_track
    
    print("Total Head Movement: ", sum(head_movement))
    print("Seek Time: ", (seek_count/num_requests))


def SSTF_time(num_processes, arrival_time, burst_time): 
    pass

def Scan_time(num_processes, arrival_time, burst_time):  
    pass

def Look_time(num_processes, arrival_time, burst_time):  
    pass

def CScan_time(num_processes, arrival_time, burst_time):  
    pass

def CLook_time(num_processes, arrival_time, burst_time):  
    pass

def input_request_locations(num_requests):
    request_locations = []
    print("Input Individual Request Location")
    for i in range(1, num_requests+1):
        req = input("Loc" +str(i) +": ")
        request_locations.append(int(req))
    return request_locations

program = True
while program == True:
    num_requests = int(input("Input no. of requests [max. of 10]: "))
    if num_requests < 1 or num_requests > 10:
        print("Must be a number between 1-10")
    else:
        current_position = int(input("Input current position: "))
        track_size = int(input("Input track size: "))
        seek_rate = int(input("Input seek rate: "))
        request_locations = input_request_locations(num_requests)
        FCFS_time(num_requests, current_position, request_locations)
    program = False

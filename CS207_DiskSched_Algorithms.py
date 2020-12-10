import math

#completion_time = []
#turnaround_time = []
#waiting_time = []
#processes = []

request_sequence = []

def get_difference(request_sequence, current_position, difference):
    for i in range(len(difference)):
        difference[i][0] = abs(request_sequence[i]-current_position)

def find_shortest_distance(difference):
    index = -1
    min = 999999999
    for i in range(len(difference)):
        if (not difference[i][1] and 
                min > difference[i][0]): 
            min = difference[i][0] 
            index = i 
    return index   

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


def SSTF_time(current_position, track_size, seek_rate, request_sequencee): 
   pass

def Scan_time(current_position, track_size, seek_rate, request_sequence):  
    pass

def Look_time(current_position, track_size, seek_rate, request_sequence):  
    pass

def CScan_time(current_position, track_size, seek_rate, request_sequence):  
    pass

def CLook_time(current_position, track_size, seek_rate, request_sequence):  
    pass



import math

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
        head_movement.append(distance)
        seek_count += distance
        current_position = current_track
    
    print("Total Head Movement: ", sum(head_movement))
    print("Seek Time: ", (seek_count/num_requests))


def SSTF_time(current_position, track_size, request_sequence): 
    if(len(request_sequence)==0):
        return
    num_request = len(request_sequence)
    difference = [0]*num_request
    
    #to initialize array
    for i in range(num_request): 
        difference[i] = [0,0]
    
    head_movement = 0       
    average_seek_time = 0
    seek_sequence = [0]*(num_request+1)
    
    for i in range(num_request):
        seek_sequence[i] = current_position
        get_difference(request_sequence, current_position, difference)
        index = find_shortest_distance(difference)
        
        difference[index][1] = True
        head_movement += difference[index][0]
        average_seek_time = head_movement/num_request
        
        current_position = request_sequence[index]
        
    seek_sequence[len(seek_sequence)-1] = current_position
    
    print("Total head movement: ", head_movement)   
    #print("Seek sequence is: ",seek_sequence)
    #for i in range(num_request+1):
    #   print(seek_sequence[i])
    print("Seek Time:", average_seek_time)

def Scan_time(head, direction, track_size, request_sequence):  
    num_request = len(request_sequence)
    head_movement, distance, current_position = 0,0,0
    left = []
    right = []
    
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(track_size-1)

    for i in range(num_request):
        if (request_sequence[i] < head):
            left.append(request_sequence[i])
        if (request_sequence[i] > head):
            right.append(request_sequence[i])
    left.sort()
    right.sort()
    run = 2
    while(run != 0):
        if(direction == "left"):
            for i in range(len(left)-1,-1,-1):
                current_position = left[i]
                request_sequence.append(current_position)
                distance = abs(current_position-head)
                head_movement += distance
                head = current_position
            direction == "right"
        elif (direction == "right"):
            for i in range(len(right)):
                current_position = right[i]
                request_sequence.append(current_position)
                distance = abs(current_position - head)
                head_movement += distance
                head = current_position
            direction = "left"
        run -= 1
    average_seek_time = head_movement/request_sequence
    print("Total head movement: ", head_movement)
    print("Seek sequence: ")
    for i in range(len(request_sequence)):
        print(request_sequence[i])
    print("Seek time: ", average_seek_time)
        

def input_request_locations(num_requests):
    request_locations = []
    print("Input Individual Request Location")
    for i in range(1, num_requests+1):
        req = input("Loc" +str(i) +": ")
        request_locations.append(int(req))
    return request_locations

# program = True
# while program == True:
#     num_requests = int(input("Input no. of requests [max. of 10]: "))
#     if num_requests < 1 or num_requests > 10:
#         print("Must be a number between 1-10")
#     else:
#         current_position = int(input("Input current position: "))
#         track_size = int(input("Input track size: "))
#         seek_rate = int(input("Input seek rate: "))
#         request_locations = input_request_locations(num_requests)
#         FCFS_time(num_requests, current_position, request_locations)
#     program = False

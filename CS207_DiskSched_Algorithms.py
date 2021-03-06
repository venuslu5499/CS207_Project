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

def FCFS_time(num_request, current_position, request_sequence):
    seek_count = 0
    distance, current_track = 0, 0
    head_movement = []

    for i in range(num_request):
        current_track = request_sequence[i] 
        distance = abs(current_track - current_position);
        head_movement.append(distance)
        seek_count += distance
        current_position = current_track
    
    print("Total Head Movement: ", sum(head_movement))
    print("Seek Time: ", (seek_count/num_request))


def SSTF_time(current_position, track_size, request_sequence): 
    if(len(request_sequence)==0):
        return
    num_request = len(request_sequence)
    difference = [0]*num_request                #initializes all elements in the array with '0'.
    
    #to initialize array
    for i in range(num_request): 
        difference[i] = [0,0]
    
    head_movement = 0       
    average_seek_time = 0
    seek_sequence = [0]*(num_request+1)                                 #initialize seek sequence array with '0'
    
    for i in range(num_request):
        seek_sequence[i] = current_position                     
        get_difference(request_sequence, current_position, difference)  #finds the minimum difference 
        index = find_shortest_distance(difference)                      #returns the index of the 
        
        difference[index][1] = True                           
        head_movement += difference[index][0]                           #solves for total head movement --  inaadd yung differences
        average_seek_time = head_movement/num_request
        
        current_position = request_sequence[index]
        
    seek_sequence[len(seek_sequence)-1] = current_position              #adds the current position(yung navisit) to the seek sequence
    
    print("Total head movement: ", head_movement)   
    print("Seek sequence is: ",seek_sequence)
    for i in range(num_request+1):
       print(seek_sequence[i])
    print("Seek Time:", average_seek_time)

def Scan_time(current_position, direction, track_size, request_sequence):  
    num_request = len(request_sequence)
    seek_count = 0
    distance, current_track = 0, 0
    head_movement = []
    left = []
    right = []
    seek_sequence = []
    
    if direction == "left":
        left.append(0)
    elif direction == "right":
        right.append(track_size-1)

    for i in range(num_request):                                #if the track is bigger than the current position
        if (request_sequence[i] < current_position):            #it gets appended to the right[] array, else 
            left.append(request_sequence[i])                    #append to left[] array
        if (request_sequence[i] > current_position):
            right.append(request_sequence[i])

    left.sort()
    right.sort()
    run = 2
    while(run != 0):
        if(direction == "left"):
            for i in range(len(left)-1,-1,-1):
                current_track = left[i]
                seek_sequence.append(current_track)
                distance = abs(current_track-current_position)
                head_movement.append(distance)
                seek_count += distance
                current_position = current_track
            direction = "right"

        elif (direction == "right"):
            for i in range(len(right)):
                current_track = right[i]
                seek_sequence.append(current_track)
                distance = abs(current_track - current_position)
                head_movement.append(distance)
                seek_count += distance
                current_position = current_track
            direction = "left"

        run -= 1

    average_seek_time = (seek_count/num_request)
    print("Total head movement: ", sum(head_movement))
    print("Seek sequence: ")
    for i in range(len(seek_sequence)):
        print(seek_sequence[i])
    print("Seek time: ", average_seek_time)


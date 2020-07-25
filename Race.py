#opeinig file
file_in = open(r"C:\Users\Micah\Desktop\Personal\Python\usaco\Race\1.in")

#getting data
metadata = file_in.readline()
race_length = metadata.split()[0]
speeds = metadata.split()[1]
speeds = int(speeds)

i = 0
all_speeds = []

while i < speeds:
    all_speeds.append(file_in.readline()[:-1])
    i += 1

#setting params
distance_traveled = 0
speed = 0

#function to see if you can slow down in time
def slow_down(speed, max_speed, distance_traveled, race_length):
    done = False
    while done == False:
        if speed <= max_speed:
            return True
        speed = speed - 1
        distance_traveled = distance_traveled + speed
        if race_length - distance_traveled <= 0:
            done = True
    if speed <= max_speed:
        return True
    else:
        return False

print(slow_down(10, 3, 0, 8))
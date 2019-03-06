from PRD import *

#''''''''''''''''''' Constants '''''''''''''''''

n = 3000 # 실험횟수

size = 20 # 격자 크기

#'''''''''''''''''''''''''''''''''''''''''''''''

On_sum = 0
Off_sum = 0

for i in range(n):
    lattice, location, loc_list = PRD(2, size, True)
    distance = abs(loc_list[0][0] - loc_list[1][0]) + abs(loc_list[1][0] - loc_list[1][1])
    On_sum += distance

for i in range(n):
    lattice, location, loc_list = PRD(2, size, False)
    distance = abs(loc_list[0][0] - loc_list[1][0]) + abs(loc_list[1][0] - loc_list[1][1])
    Off_sum += distance

On_avg = On_sum / n
Off_avg = Off_sum / n

print("On : "+ str(On_avg))
print("Off : "+ str(Off_avg))

    

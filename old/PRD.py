#'''''''''''''''''''''''''''''''''''''''''''''''
#'''' Pseudo Random Distribution Simulator '''''
#''''                                      '''''
#'''''''''''''''''''''''''''''''''''''''''''''''

from random import *

#''''''''''''''''''' Constants '''''''''''''''''

n = 30 # 시행횟수

size = 20 # 격자 크기

OnOff = True # PRD 적용 여부

#'''''''''''''''''''''''''''''''''''''''''''''''

def print_array(array):
    size = len(array)
    for i in range(size):
        print(array[i])
        
#'''''''''''''''''''''''''''''''''''''''''''''''
def PRD(n, size, OnOff):
    lattice = [[100 for col in range(size)] for row in range(size)]

    location = [[' ' for col in range(size)] for row in range(size)]

    loc_list = []

    for i in range(n):
        rowsum = [0] * size

        for j in range(size):
            for k in range(size):
                rowsum[j] += lattice[j][k]
                
        totalsum = 0
        for j in range(size):
            totalsum += rowsum[j]

        randomnumber = random() * totalsum

        counter = 0
        temp_rowsum = rowsum[counter]
        temp_prevrowsum = 0
        while (temp_rowsum < randomnumber):
            temp_prevrowsum += rowsum[counter]
            counter += 1
            temp_rowsum += rowsum[counter]

        counter2 = 0
        temp_column = lattice[counter][counter2]
        while (temp_column + temp_prevrowsum < randomnumber):
            counter2 += 1
            temp_column += lattice[counter][counter2]

        location[counter][counter2] = 'O'

        lattice[counter][counter2] = 0

        loc_list.append((counter, counter2))

        if OnOff:
            locX = counter
            locY = counter2

            for j in range(size):
                for k in range(size):
                    disX = abs(locX - j)
                    disY = abs(locY - k)
                    distance = disX + disY

                    if distance == 1:
                        lattice[j][k] *= 0.05
                    elif distance == 2:
                        lattice[j][k] *= 0.1
                    elif distance == 3:
                        lattice[j][k] *= 0.2
                    elif distance == 4:
                        lattice[j][k] *= 0.5
                    elif distance == 5:
                        lattice[j][k] *= 0.9
                    elif distance == 6:
                        lattice[j][k] *= 1
                        
    return lattice, location, loc_list

if __name__ == '__main__':
    lattice, location, loc_list = PRD(n, size, OnOff)
    print_array(lattice)
    print()
    print_array(location)

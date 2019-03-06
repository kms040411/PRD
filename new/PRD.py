#'''''''''''''''''''''''''''''''''''''''''''''''
#'''' Pseudo Random Distribution Simulator '''''
#''''                                      '''''
#'''''''''''''''''''''''''''''''''''''''''''''''

from random import *
from math import *

#''''''''''''''''' Test Case '''''''''''''''''''

n = 50 # 시행횟수

OnOff = False # PRD 적용 여부

step = False # 각 시행마다 출력

prob = 30 # 확률(%, int)

print_mode = True # 함수에서 결과를 직접 출력

comp = True # PRD 적용/비적용 비교

#'''''''''''''''''''''''''''''''''''''''''''''''

def PRD(n, OnOff, step, prob, print_mode):
    array = [0 for row in range(n)]
    current_prob = prob
    Ostreak = 0
    Xstreak = 0

    if print_mode:
        print("Result: ", end="")

    for i in range(n):
        if not OnOff:
            result = prob_random(prob)
            if result:
                array[i] = "O"
            else:
                array[i] = "X"
        else:
            result = prob_random(current_prob)
            if result:
                array[i] = "O"
                Ostreak = Ostreak + 2
                Xstreak = 0
            else:
                array[i] = "X"
                Ostreak = 0
                Xstreak = Xstreak + 1
            current_prob = calc_Next_Prob(Ostreak, Xstreak, prob)

        if step and print_mode:
            if i != n-1:
                print(array[i] + ", ", end="")
            else:
                print(array[i])
    
    for i in range(n):
        if i != n-1:
            print(array[i] + ", ", end="")
        else:
            print(array[i])
    print("")
    return array

def prob_random(prob):
    randomnumber = random() * 100
    if randomnumber < prob:
        return True
    else:
        return False

def statistic(array, OnOff):
    print("=== Statistic ===")
    print("n : " + str(n))
    if OnOff:
        print("PRD : On")
    else:
        print("PRD : Off")

    length = len(array)
    Os = 0
    Xs = 0

    for i in range(length):
        if array[i] == "O":
            Os = Os + 1
        else:
            Xs = Xs + 1

    print("Probability: " + str(calc_stat_prob(Os, Xs)))
    
    distance_list = list()
    Ostreak = 0
    for i in range(length):
        if array[i] == "O":
            distance_list.append(Ostreak)
            Ostreak = 0
        else:
            Ostreak = Ostreak + 1

    print("Distribution: " + str(calc_stat_dist(distance_list)))
    print("")
    
def calc_stat_prob(Os, Xs):
    return Os / (Os + Xs)

def calc_stat_dist(distance_list):
    sum = 0
    for i in range(len(distance_list)):
        sum = sum + distance_list[i] * distance_list[i]
    return sqrt(sum / len(distance_list))

def calc_Next_Prob(Ostreak, Xstreak, prob):
    next_prob = prob
    next_prob = next_prob - prob * 3 / 10 * Ostreak
    next_prob = next_prob + prob * 3 / 10 * Xstreak
    return next_prob
    
if __name__ == "__main__":
    if comp:
        array1 = PRD(n, True, step, prob, print_mode)
        array2 = PRD(n, False, step, prob, print_mode)
        statistic(array1, True)
        statistic(array2, False)
    else:
        array = PRD(n, OnOff, step, prob, print_mode)
        statistic(array, OnOff)
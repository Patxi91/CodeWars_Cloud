'''
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

def snail(snail_map):
    #print(snail_map)
    sol = []
    if snail_map == [[]]:
        return sol
    lenght = len(snail_map)**2
    while len(sol)< lenght:
        if len(sol)< lenght:
            snail_map , sol = go_right(snail_map,sol)
        if len(sol)< lenght:
            snail_map , sol = go_down(snail_map,sol)
        if len(sol)< lenght:
            snail_map , sol=go_left(snail_map,sol)
        if len(sol)< lenght:
            snail_map, sol = go_up(snail_map,sol)

    return sol

def go_right(snail_map,sol):
    lenght = len(snail_map[0])
    for i in range(lenght):
        sol.append(snail_map[0][i])
    snail_map.pop(0)
    return snail_map,sol

def go_down(snail_map,sol):
    lenght = len(snail_map)
    for i in range(lenght):
        sol.append(snail_map[i][len(snail_map[i])-1])
        snail_map[i].pop(len(snail_map[i])-1)
    return snail_map,sol
        
def go_left(snail_map,sol):

    for i in reversed(snail_map[len(snail_map)-1]):
        sol.append(i)
    snail_map.pop(len(snail_map)-1)
    return snail_map,sol

def go_up(snail_map,sol):
    lenght = len(snail_map)
    for i in range(1,lenght):
        sol.append(snail_map[-i][0])
        snail_map[-i].pop(0)

    return snail_map,sol


array = [[384, 562, 760, 249, 190, 392, 758, 424, 989, 13], [90, 653, 855, 273, 649, 632, 951, 159, 692, 171], [662, 751, 836, 901, 511, 735, 197, 12, 631, 408], [464, 375, 324, 586, 807, 206, 809, 638, 283, 421], [731, 178, 806, 304, 725, 510, 476, 20, 674, 253], [59, 590, 332, 973, 861, 796, 630, 125, 690, 833], [16, 513, 857, 780, 482, 563, 314, 861, 115, 920], [325, 38, 922, 278, 142, 24, 304, 312, 54, 127], [904, 717, 855, 106, 833, 119, 478, 278, 941, 301], [235, 150, 518, 185, 809, 833, 866, 304, 371, 451]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))
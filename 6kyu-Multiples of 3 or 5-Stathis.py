def solution(number):
    i = 3
    j = 5
    list = []
    while i< number:
        #print(i,' ')
        list.append(i)
        i = i + 3
        
    while j < number:
        #print(j,' ')
        list.append(j)
        j = j + 5
    set_list = set(list)
    return sum(set_list)

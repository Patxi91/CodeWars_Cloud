import numpy as np
def spiralize(size):
    
    spiral = np.zeros((size, size), dtype=int)
    spiral[0] = 1
    node = (0,size-1)
    directions = [(1,0),(0,-1),(-1,0),(0,1)]
    end = True
    edges =[(0,0),(size-1,size-1),(size-1,0),(0,size-1)]
    while end:
        end = False
        for dx, dy in directions:
            '''print(dx,dy)'''
            while (0<= node[0]+dx < size and -0<= node[1]+dy < size and node[0]+dx+dx< size and node[1]+dy+dy< size  and spiral[node[0]+dx+dx][node[1]+dy+dy] != 1):
                isOK = True
                for value in directions:
                    if (value != (-dx,-dy) and 0<node[0]+dx+value[0] < size and 0<node[1]+dy+value[1]< size and spiral[node[0]+dx+value[0]][node[1]+dy+value[1]]==1):
                 
                        isOK = False
                        end = False
                        node = (node[0]+dx,node[1]+dy)
                        
                if isOK:
                 
                    node = (node[0]+dx,node[1]+dy)
                    spiral[node[0]][node[1]] = 1
                    end =True
                    
                
                  
            if(0<= node[0]+dx < size and 0<= node[1]+dy < size)and((node[0]+dx,node[1]+dy) in edges):
           
                node = (node[0]+dx,node[1]+dy)
                spiral[node[0]][node[1]] = 1
                end =True
           

    return spiral.tolist()





print(spiralize(42))
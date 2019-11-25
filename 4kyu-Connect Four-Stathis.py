def check_winner(grid):
    for i in range(7):
        for j in range(6):
            if grid[i][j] != ' ':
                if j+3 < 6:
                    if grid[i][j]==grid[i][j+1]==grid[i][j+2]==grid[i][j+3]:
                        return grid[i][j]
                if i+3 < 7 and j+3 < 6:
                    if grid[i][j]==grid[i+1][j+1]==grid[i+2][j+2]==grid[i+3][j+3]:
                        return grid[i][j]
                if i-3 >= 0 and j+3 >= 0:
                    if grid[i][j]==grid[i-1][j+1]==grid[i-2][j+2]==grid[i-3][j+3]:
                        return grid[i][j]
                if i+3 < 7:
                    if grid[i][j]==grid[i+1][j]==grid[i+2][j]==grid[i+3][j]:
                        return grid[i][j]
                  
                    
def who_is_winner(pieces_position_list):  
    grid=[[],[],[],[],[],[],[]]
    for position in pieces_position_list:
        grid['ABCDEFG'.index(position[0])].append(position[2:])        
    
    
        grid2 = []
        for c in range(0,7):
            grid2.append([])
            for r in range(0,7):
                grid2[c].append(grid[c][r] if r < len(grid[c]) else ' ')
        if check_winner(grid2) != None:
            return check_winner(grid2)      
    return 'Draw'

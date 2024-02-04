def cube_matrix_sum(m):return sum(sum(sum(m,[]),[]))  # l=52
def cube_matrix_sum(m): return sum(map(sum, m))  # l=47
def cube_matrix_sum(m):(r:=sum(sum(m,[]),[]))  # l=45
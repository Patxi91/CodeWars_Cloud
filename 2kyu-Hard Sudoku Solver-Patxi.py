BLOCK_SIZE = 3
FIELD_SIZE = 9

class NoAvailableValue(Exception):
    pass


class NoSolution(Exception):
    pass


class MultipleSolution(Exception):
    pass


def copy_p(p):
    return [[i for i in line] for line in p]

def sudoku_solver(puzzle):

    f_range = range(FIELD_SIZE)
    b_range = range(BLOCK_SIZE)
    d_set = set(range(1, FIELD_SIZE + 1))

    def puzzle_validator(p):
        if len(p) != FIELD_SIZE:
            raise ValueError
        for line in p:
            if not set(line).issubset(d_set | {0}):
                raise ValueError
            if len(line) != FIELD_SIZE:
                raise ValueError

    def iter_field():
        for i in f_range:
            for j in f_range:
                yield i, j

    def get_block_points(b_i, b_j):
        return [(b_i*BLOCK_SIZE + i, b_j*BLOCK_SIZE + j) for i in b_range for j in b_range]

    def iter_block():
        for b_i in b_range:
            for b_j in b_range:
                yield b_i, b_j

    def get_block_ij(i, j):
        return i // BLOCK_SIZE, j // BLOCK_SIZE

    def get_v_points(i):
        return [(k, i) for k in f_range]

    def get_h_points(i):
        return [(i, k) for k in f_range]

    def get_v_set(p, i):
        return {x for k in f_range if isinstance((x := p[k][i]), int) and x != 0}

    def get_h_set(p, i):
        return {x for k in f_range if isinstance((x := p[i][k]), int) and x != 0}

    def get_block_set(p, b_i, b_j):
        block_points = get_block_points(b_i, b_j)
        return {x for i in block_points if isinstance((x := p[i[0]][i[1]]), int) and x != 0}

    def get_available_set(p, i, j):
        block_set = get_block_set(p, *get_block_ij(i, j))
        available_set = d_set - (get_v_set(p, j) | get_h_set(p, i) | block_set)

        if len(available_set) == 0:
            raise NoAvailableValue

        return available_set

    def is_solved(p):
        for i, j in iter_field():
            if get_v_set(p, j) != d_set or get_h_set(p, i) != d_set:
                return False
        for b_i, b_j in iter_block():
            if get_block_set(p, b_i, b_j) != d_set:
                return False
        return True

    def iter_field_set_val(p):
        for i, j in iter_field():
            if isinstance(p[i][j], set):
                yield i, j, p[i][j]

    def calc_available_set(p):
        for i, j in iter_field():
            if p[i][j] not in d_set:
                p[i][j] = get_available_set(p, i, j)
        return p

    def remove_val_from_available_set(p, i, j, val):
        h_points = get_h_points(i)
        v_points = get_v_points(j)
        block_points = get_block_points(*get_block_ij(i, j))
        points = set(h_points + v_points + block_points)
        for p_i, p_j in points:
            if isinstance(p[p_i][p_j], set):
                if len(p[p_i][p_j] - {val}) == 0:
                    raise NoAvailableValue
                p[p_i][p_j] = p[p_i][p_j] - {val}
        return p

    def solver(p):

        if is_solved(p):
            solutions.append(p)
            if len(solutions) > 1:
                raise MultipleSolution
            return
        try:
            i_min, j_min, p_set = min(iter_field_set_val(p), key=lambda x: len(x[2]))
        except ValueError:
            raise NoSolution

        for val in p_set:
            new_p = copy_p(p)
            new_p[i_min][j_min] = val
            try:
                new_p = remove_val_from_available_set(new_p, i_min, j_min, val)
            except NoAvailableValue:
                continue
            if is_solved(new_p):
                solutions.append(new_p)
                if len(solutions) > 1:
                    raise MultipleSolution
                return
            try:
                solver(new_p)
            except NoSolution:
                continue
        if not solutions:
            raise NoSolution

    solutions = []
    puzzle_validator(puzzle)
    p = calc_available_set(puzzle)
    solver(p)

    if len(solutions) == 0:
        raise NoSolution
    return solutions[0]

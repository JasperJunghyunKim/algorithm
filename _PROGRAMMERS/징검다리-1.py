
def solution(arrows):
    cur_r, cur_c = 0, 0
    visited_vertex = {(0, 0): True}
    visited_edge = dict()
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    num_rooms = 0
    for arrow in arrows:
        dr, dc = directions[arrow]
        next_r, next_c = cur_r + dr, cur_c + dc
        next_mid_r, next_mid_c = 0, 0
        if arrow in {1, 3, 5, 7}:
            next_mid_r, next_mid_c = cur_r + (0.5 * dr), cur_c + (0.5 * dc)
            if (next_mid_r, next_mid_c) not in visited_vertex:
                visited_vertex[(next_mid_r, next_mid_c)] = True
            else:
                if ((next_r, next_c, cur_r, cur_c) not in visited_edge) and (
                        (cur_r, cur_c, next_r, next_c) not in visited_edge):
                    num_rooms += 1
        if (next_r, next_c) not in visited_vertex:
            visited_vertex[(next_r, next_c)] = True
            visited_edge[(next_r, next_c, cur_r, cur_c)] = True
        else:
            if ((next_r, next_c, cur_r, cur_c) not in visited_edge) and ((cur_r, cur_c, next_r, next_c) not in visited_edge):
                visited_edge[(next_r, next_c, cur_r, cur_c)] = True
                num_rooms += 1
        cur_r, cur_c = next_r, next_c
    return num_rooms

# arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0]
# arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0]
# arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
# arrows = [6, 4, 2, 6, 1, 6, 3]
arrows = [6, 4, 2, 0, 5, 2, 7, 2, 6, 4, 2, 0, 5, 2, 7, 2]
print(solution(arrows))
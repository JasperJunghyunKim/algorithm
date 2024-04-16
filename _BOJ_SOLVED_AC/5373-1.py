import sys
sys_input = sys.stdin.readline
CLOCK = 1
COUNTERCLOCK = -1
cube_bp = [['' for _ in range(9)] for _ in range(12)]

def init():
    for r in range(3, 6):
        for c in range(0, 3):
            cube_bp[r][c] = 'g'
    for r in range(0, 0+3):
        for c in range(3, 6):
            cube_bp[r][c] = 'o'
    for r in range(3, 6):
        for c in range(3, 6):
            cube_bp[r][c] = 'w'
    for r in range(6, 9):
        for c in range(3, 6):
            cube_bp[r][c] = 'r'
    for r in range(9, 12):
        for c in range(3, 6):
            cube_bp[r][c] = 'y'
    for r in range(3, 6):
        for c in range(6, 9):
            cube_bp[r][c] = 'b'

def rotate_surface(d, r, c):
    new_bp = [[0 for _ in range(3)] for _ in range(3)]
    for dr in range(r, r+3):
        for dc in range(c, c+3):
                new_bp[dr-r][dc-c] = cube_bp[dr][dc]
    if d == CLOCK:
        for dr in range(3):
            for dc in range(3):
                cube_bp[r + dc][c + (2 - dr)] = new_bp[dr][dc]
    if d == COUNTERCLOCK:
        for dr in range(3):
            for dc in range(3):
                cube_bp[r + (2 - dc)][c + dr] = new_bp[dr][dc]

def rotate_top(d):
    
    rotate_surface(d, 3, 3)
    back_top = cube_bp[2][3:6]
    right_top = [cube_bp[i][6] for i in range(5, 2, -1)]
    front_top = cube_bp[6][3:6]
    left_top = [cube_bp[i][2] for i in range(5, 2, -1)]
    
    for i in range(3):
        cube_bp[2][3+i] = left_top[i] if d == CLOCK else right_top[i]
        cube_bp[3+i][6] = back_top[i] if d == CLOCK else front_top[i]
        cube_bp[6][3+i] = right_top[i] if d == CLOCK else left_top[i]
        cube_bp[3+i][2] = front_top[i] if d == CLOCK else back_top[i]
        
def rotate_left(d):
    rotate_surface(d, 3, 0)
    back_top = [cube_bp[i][3] for i in range(0, 3)]
    top_top = [cube_bp[i][3] for i in range(3, 6)]
    front_top = [cube_bp[i][3] for i in range(6, 9)]
    bottom_top = [cube_bp[i][3] for i in range(9, 12)]
    
    for i in range(3):
        cube_bp[0 + i][3] = bottom_top[i] if d == CLOCK else top_top[i]
        cube_bp[3 + i][3] = back_top[i] if d == CLOCK else front_top[i]
        cube_bp[6 + i][3] = top_top[i] if d == CLOCK else bottom_top[i]
        cube_bp[9 + i][3] = front_top[i] if d == CLOCK else back_top[i]
        
def rotate_right(d):
    rotate_surface(d, 3, 6)
    back_top = [cube_bp[i][5] for i in range(0, 3)]
    top_top = [cube_bp[i][5] for i in range(3, 6)]
    front_top = [cube_bp[i][5] for i in range(6, 9)]
    bottom_top = [cube_bp[i][5] for i in range(9, 12)]
        
    for i in range(3):
            cube_bp[0 + i][3] = top_top[i] if d == CLOCK else bottom_top[i]
            cube_bp[3 + i][3] = front_top[i] if d == CLOCK else back_top[i]
            cube_bp[6 + i][3] = bottom_top[i] if d == CLOCK else top_top[i]
            cube_bp[9 + i][3] = back_top[i] if d == CLOCK else front_top[i]


def rotate_front(d):
    rotate_surface(d, 6, 3)
    left_top = cube_bp[5][0:3]
    top_top = cube_bp[5][3:6]
    right_top = cube_bp[5][6:9]
    bottom_top = cube_bp[9][3:6]
    
    for i in range(3):
        cube_bp[5][0 + i] = list(reversed(bottom_top))[i] if d == CLOCK else top_top[i]
        cube_bp[5][3 + i] = left_top[i] if d == CLOCK else right_top[i]
        cube_bp[5][6 + i] = top_top[i] if d == CLOCK else list(reversed(bottom_top))[i]
        cube_bp[9][3 + i] = list(reversed(right_top))[i] if d == CLOCK else list(reversed(left_top))[i]

def rotate_back(d):
    rotate_surface(d, 0, 3)
    left_top = cube_bp[3][0:3]
    top_top = cube_bp[3][3:6]
    right_top = cube_bp[3][6:9]
    bottom_top = cube_bp[11][3:6]
    
    for i in range(3):
        cube_bp[3][0 + i] = list(reversed(bottom_top))[i] if d == COUNTERCLOCK else top_top[i]
        cube_bp[3][3 + i] = left_top[i] if d == COUNTERCLOCK else right_top[i]
        cube_bp[3][6 + i] = top_top[i] if d == COUNTERCLOCK else list(reversed(bottom_top))[i]
        cube_bp[11][3 + i] = list(reversed(right_top))[i] if d == COUNTERCLOCK else list(reversed(left_top))[i]
        
def rotate_bottom(d):
    rotate_surface(d, 9, 3)
    back_top = cube_bp[0][3:6]
    right_top = [cube_bp[i][8] for i in range(3, 6)]
    front_top = list(reversed(cube_bp[8][3:6]))
    left_top = [cube_bp[i][0] for i in range(5, 2, -1)]
    
    for i in range(3):
        cube_bp[0][3 + i] = left_top[i] if d == COUNTERCLOCK else right_top[i]
        cube_bp[3 + i][8] = back_top[i] if d == COUNTERCLOCK else front_top[i]
        cube_bp[8][5 - i] = right_top[i] if d == COUNTERCLOCK else left_top[i]
        cube_bp[5 - i][0] = front_top[i] if d == COUNTERCLOCK else back_top[i]
        
# def roll_back():
#     new_cube_bp = [['' for _ in range(9)] for _ in range(12)]
#     for r in range(12):
#         for c in range(9):
#             if 0 <= c < 3 or 6 <= c < 9:
#                 new_cube_bp[r][c] = cube_bp[r][c]
#     for r in range(3, 12):
#         for c in range(3, 6):
#             new_cube_bp[r-3][c] = cube_bp[r][c]
#     for r in range(3):
#         for c in range(3, 6):
#             new_cube_bp[r+9][c] = cube_bp[r][c]
#     rotate_surface(COUNTERCLOCK, 3, 0)
#     rotate_surface(CLOCK, 3, 6)
#     return new_cube_bp

# def roll_front():
#     new_cube_bp = [['' for _ in range(9)] for _ in range(12)]
#     for r in range(12):
#         for c in range(9):
#             if 0 <= c < 3 or 6 <= c < 9:
#                 new_cube_bp[r][c] = cube_bp[r][c]
#     for r in range(0, 9):
#         for c in range(3, 6):
#             new_cube_bp[r+3][c] = cube_bp[r][c]
#     for r in range(9, 12):
#         for c in range(3, 6):
#             new_cube_bp[r-9][c] = cube_bp[r][c]
#     rotate_surface(CLOCK, 3, 0)
#     rotate_surface(COUNTERCLOCK, 3, 6)
#     return new_cube_bp

# def roll_right():
#     new_cube_bp = [['' for _ in range(9)] for _ in range(12)]
#     for r in range(12):
#         for c in range(9):
#             if 0 <= r < 3 or 6 <= r < 9:
#                 new_cube_bp[r][c] = cube_bp[r][c]
#     # shift right
#     for r in range(3, 6):
#         for c in range(6):
#             new_cube_bp[r][c+3] = cube_bp[r][c]
#     # right -> bottom
#     for r in range(3, 6):
#         for c in range(6, 9):
#             new_cube_bp[11-(r-3)][5-(c-6)] = cube_bp[r][c]
#     # bottom -> left
#     for r in range(9,12):
#         for c in range(3,6):
#             new_cube_bp[5-(r-9)][2-(c-3)] = cube_bp[r][c]
            
#     rotate_surface(COUNTERCLOCK, 0, 3)
#     rotate_surface(CLOCK, 6, 3)
#     return new_cube_bp

# def roll_left():
#     new_cube_bp = [['' for _ in range(9)] for _ in range(12)]
#     for r in range(12):
#         for c in range(9):
#             if 0 <= r < 3 or 6 <= r < 9:
#                 new_cube_bp[r][c] = cube_bp[r][c]
#     # shift left
#     for r in range(3, 6):
#         for c in range(3,9):
#             new_cube_bp[r][c-3] = cube_bp[r][c]
#     # left -> bottom
#     for r in range(3, 6):
#         for c in range(3):
#             new_cube_bp[11-(r-3)][5-(c)] = cube_bp[r][c]
#     # bottom -> right
#     for r in range(9,12):
#         for c in range(3,6):
#             new_cube_bp[5-(r-9)][8-(c-3)] = cube_bp[r][c]
#     rotate_surface(CLOCK, 0, 3)
#     rotate_surface(COUNTERCLOCK, 6, 3)
#     return new_cube_bp

def print_top():
    for r in range(3,6):
        print(*cube_bp[r][3:6], sep="")
          
init()  


N = int(sys_input().strip())
for _ in range(N):
    num_cmd = int(sys_input().strip())
    cmd_list= sys_input().strip().split()
    for cmd in cmd_list:
        if cmd == "L-":
            rotate_left(COUNTERCLOCK)
        elif cmd == "L+":
            rotate_left(CLOCK)
        elif cmd == "R-":
            rotate_right(COUNTERCLOCK)
        elif cmd == "R+":
            rotate_right(CLOCK)
        elif cmd == "U-":
            rotate_top(COUNTERCLOCK)
        elif cmd == "U+":
            rotate_top(CLOCK)
        elif cmd == "D-":
            rotate_bottom(COUNTERCLOCK)
        elif cmd == "D+":
            rotate_bottom(CLOCK)
        elif cmd == "B-":
            rotate_back(COUNTERCLOCK)
        elif cmd == "B+":
            rotate_back(CLOCK)
        elif cmd == "F-":
            rotate_front(COUNTERCLOCK)
        elif cmd == "F+":
            rotate_front(CLOCK)

    print_top()


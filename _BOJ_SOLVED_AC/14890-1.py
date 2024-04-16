import sys
sys_input = sys.stdin.readline

SIZE_MAP, SIZE_STEEP = map(int, sys_input().strip().split())
road_map = [list(map(int, sys_input().strip().split())) for _ in range(SIZE_MAP)]
steep_map_row = [[False] * SIZE_MAP for _ in range(SIZE_MAP)]
g_num_roads = 0

def find_row_roads():
    global g_num_roads
    num_roads = 0
    
    # ROW_ROAD
    for r in range(SIZE_MAP):
        road = True
        
        for c in range(SIZE_MAP):
            if road == False:
                break
            # 우하향        
            if c != SIZE_MAP - 1:
                if abs(road_map[r][c] - road_map[r][c+1]) >= 2:
                    road = False
                    break
                if road_map[r][c] == road_map[r][c + 1] + 1:
                    if c + SIZE_STEEP >= SIZE_MAP:
                        road = False
                        break
                    else:
                        for d_c in range(c + 1, c + SIZE_STEEP + 1):
                            if steep_map_row[r][d_c]:
                                road = False
                                break
                            else:
                                if d_c != c + SIZE_STEEP and road_map[r][d_c] != road_map[r][d_c + 1]:
                                    road = False
                                    break
                        for d_c in range(c + 1, c + SIZE_STEEP + 1):
                            steep_map_row[r][d_c] = True                      
                    
            # 좌하향
            if c != 0:
                if abs(road_map[r][c] - road_map[r][c-1]) >= 2:
                    road = False
                    break
                if road_map[r][c] == road_map[r][c - 1] + 1:
                    if c - SIZE_STEEP < 0:
                        road = False
                        break
                    else:
                        for d_c in range(c - 1, c - SIZE_STEEP - 1, -1):
                            if steep_map_row[r][d_c]:
                                road = False
                                break
                            else:
                                if d_c != c - SIZE_STEEP and road_map[r][d_c] != road_map[r][d_c - 1]:
                                    road = False
                                    break
                        for d_c in range(c - 1, c - SIZE_STEEP -1, -1):
                            steep_map_row[r][d_c] = True 
            
        if road == True:
            g_num_roads += 1

def rotate():
    global road_map
    new_map = [[0] * SIZE_MAP for _ in range(SIZE_MAP)]
    for r in range(SIZE_MAP):
        for c in range(SIZE_MAP):
            new_map[c][SIZE_MAP - 1 - r] = road_map[r][c]
    road_map = [i[::] for i in new_map]
                
find_row_roads()
rotate()
steep_map_row = [[False] * SIZE_MAP for _ in range(SIZE_MAP)]
find_row_roads()
print(g_num_roads)
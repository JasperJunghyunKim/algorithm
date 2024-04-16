import sys
sys_input = sys.stdin.readline

SIZE, MAX_OPENED = map(int, sys_input().strip().split())
chicken_city = [list(map(int, sys_input().strip().split())) for _ in range(SIZE)]
houses = []
stores = []
min_chicken_score = float('inf')

for r in range(SIZE):
    for c in range(SIZE):
        if chicken_city[r][c] == 1:
            houses.append((r,c))
        elif chicken_city[r][c] == 2:
            stores.append((r,c))

NUM_STORES = len(stores)
NUM_HOUSES = len(houses)

def find_chicken_score(l):
    global min_chicken_score
    city_score = 0
    for house_r, house_c in houses:
        house_score = float('inf')
        for store_r, store_c in l:
        # for i, (store_r, store_c) in enumerate(stores):
        #     if not opened_stores[i]: continue
            tmp = abs(house_r - store_r) + abs(house_c - store_c)
            house_score = tmp if tmp < house_score else house_score
        city_score += house_score
        if city_score > min_chicken_score: return
    min_chicken_score = city_score if city_score < min_chicken_score else min_chicken_score

# opened_stores = [False for _ in range(NUM_STORES)]
def combination(l, length, r, idx):
    if length == r:
        find_chicken_score(l)
        return
    for i in range(idx, NUM_STORES):
        # opened_stores[i] = True
        combination(l + [stores[i]], length + 1, r, i + 1)
        # opened_stores[i] = False
        

for r in range(MAX_OPENED + 1):
    combination([], 0, r, 0)

print(min_chicken_score)
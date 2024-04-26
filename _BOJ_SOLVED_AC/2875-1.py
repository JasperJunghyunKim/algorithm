import sys
GIRLS, BOYS, INTERNS = map(int, sys.stdin.readline().strip().split())

def find_max_teams():
    num_teams = 0
    if GIRLS >= BOYS * 2:
        num_teams += BOYS
        to_interns = GIRLS - BOYS * 2
        if to_interns >= INTERNS:
            return num_teams
        else:
            if (INTERNS - to_interns) % 3 == 0:
                num_teams -= (INTERNS - to_interns) // 3
            else:
                num_teams -= (INTERNS - to_interns) // 3
                num_teams -= 1
            return num_teams
    else:
        num_teams += GIRLS // 2
        to_interns = 0
        if GIRLS % 2 == 1:
            to_interns = 1
        to_interns += BOYS - GIRLS // 2
        if to_interns >= INTERNS:
            return num_teams
        else:
            if (INTERNS - to_interns) % 3 == 0:
                num_teams -= (INTERNS - to_interns) // 3
            else:
                num_teams -= (INTERNS - to_interns) // 3
                num_teams -= 1
            return num_teams

num_teams = find_max_teams()
if num_teams <= 0:
    print(0)
else:
    print(num_teams)






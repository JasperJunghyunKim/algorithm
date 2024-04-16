import sys
sys_input = sys.stdin.readline

def find(to_find):
    if board[0] == to_find and board[1] == to_find and board[2] == to_find: return True
    if board[3] == to_find and board[4] == to_find and board[5] == to_find: return True
    if board[6] == to_find and board[7] == to_find and board[8] == to_find: return True
    
    if board[0] == to_find and board[3] == to_find and board[6] == to_find: return True
    if board[1] == to_find and board[4] == to_find and board[7] == to_find: return True
    if board[2] == to_find and board[5] == to_find and board[8] == to_find: return True
    
    if board[0] == to_find and board[4] == to_find and board[8] == to_find: return True
    if board[2] == to_find and board[4] == to_find and board[6] == to_find: return True
    return False

#
# T2
# T1 에서는 경우를 나누는 게 복잡했음 -> valid, invalid 찾는 게 복잡했음
# T2 처럼 valid 한 경우만 찾고, 나머지는 invalid 로 처리하는 게 깔끔
#
while True:
    board = sys_input().strip()
    # EXIT 인 경우
    if board == "end":
        exit()
    
    num_o = board.count("O")
    num_x = board.count("X")   
    board = list(board) 
    # X 가 이기는 경우
    # X 3줄, O 3줄 없어야함, X가 1개 더 많아야 함
    if find("X") and not find("O") and num_x == num_o + 1:
        print("valid")
        continue
    
    # O 가 이기는 경우
    # O 3줄, X 3줄 없어야함, XO 갯수가 같아야 함
    if find("O") and not find("X") and num_x == num_o:
        print("valid")
        continue
    
    # 비기는 경우
    # X == 5, O == 4, 둘 다 3 줄이 없어야 함
    if not find("O") and not find("X") and num_x == 5 and num_o == 4:
        print("valid")
        continue
    
    # 그 외는 invalid
    print("invalid")
    

# 
# T1
#
# while True:
#     board = sys_input().strip()
#     # EXIT 인 경우
#     if board == "end":
#         exit()
#     board = list(board)
    
#     num_o = board.count("O")
#     num_x = board.count("X")
#     num_blank = board.count(".")
    
#     # 순서상 배치가 불가능한 경우
#     # O 가 더 많은 경우
#     # X 가 2 개 이상 많은 경우
#     if num_o > num_x:
#         print("invalid")
#         continue
#     if num_x >= num_o + 2:
#         print("invalid")
#         continue   
    
#     # 홀수개에서(X가놓을차례) O 가 이미 한 줄 생성
#     # 짝수개에서(O가놓을차례) X 가 이미 한 줄 생성
#     prev_turn = "O" if num_blank % 2 == 0 else "X"
#     this_turn = "X" if num_blank % 2 == 0 else "O"
    
#     if find(prev_turn): 
#         print("invaid")
#         continue
#     if find(this_turn): 
#         print("valid")
#         continue
    
#     # 9개 모두 배치된 경우
#     if num_blank == 0:
#         print("valid")
#         continue
#     else:
#         print("invalid")
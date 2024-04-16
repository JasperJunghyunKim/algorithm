#
# 24-03-19
# 여행경로-3.py 의 T1 코드가 직관적이지 않아서 다시 시도
#

def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    tickets_used = [False] * len(tickets)
    
    def dfs(cur_city, path):
        
        if len(path) == len(tickets) + 1:
            return path
        
        for t_no, (dept, arrv) in enumerate(tickets):
            if cur_city == dept and not tickets_used[t_no]:
                tickets_used[t_no] = True
                
                # path.append(arrv)
                # result = dfs(arrv, path)
                result = dfs(arrv, path + [arrv])
                
                if result: return result
                tickets_used[t_no] = False
        return False
    
    return dfs("ICN", ["ICN"])
NUM_TICKETS = None
ticket_used = None
path = []
def recursive(tickets, num_tickets_used, bounds):
    global path
    if num_tickets_used == NUM_TICKETS:
        if not path:
            path = bounds
        else:
            path = bounds if bounds < path else path
        return
    for idx, ticket in enumerate(tickets):
        if not ticket_used[idx] and ticket[0] == bounds[-1]:
            ticket_used[idx] = True
            recursive(tickets, num_tickets_used + 1, bounds + [ticket[1]])
            ticket_used[idx] = False

def solution(tickets):
    global NUM_TICKETS
    global ticket_used
    NUM_TICKETS = len(tickets)
    ticket_used = [False] * len(tickets)

    recursive(tickets, 0, ["ICN"])
    return path

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)
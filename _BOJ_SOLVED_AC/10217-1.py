import sys
import heapq
sys_input = sys.stdin.readline

NUM_TC = int(sys_input())
NUM_PORTS, MAX_PRICE, NUM_TICKETS = map(int, sys_input().split())
adj_list = [[] for _ in range(NUM_PORTS + 1)]
for _ in range(NUM_TICKETS):
    port_from, port_to, cost, time = map(int, sys_input().split())
    adj_list[port_from].append(port_to, cost, time)


def dijkstra(start_port, num_ports):
    minimum = {i:[] for i in range(1, num_ports + 1)}
    minimum[start_port].append((0, 0))
    
    pq = [(0, 0)]
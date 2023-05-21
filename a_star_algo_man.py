import heapq

class Queue(object):
    def __init__(self):
        self.elements = []

    def length(self):
        return len(self.elements)

    def push(self, x, priority):
        heapq.heappush(self.elements, (priority, x))

    def pop(self):
        return heapq.heappop(self.elements)[1]

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 3, 0, 0, 0, 0, 2, 0, 1, 0],
        [0, 3, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (1, 5)
goal = (8, 1)

queue = Queue()
queue.push(start, 0)
came_from = {}
cost_so_far = {}
cost_so_far[start] = 0

def calc_cost(current, next):
    (x, y) = next
    return cost_so_far[current] + grid[y][x]

def heuristic(goal, next):
    (x1, y1) = goal
    (x2, y2) = next
    dx = abs(x1 - x2)  # x 좌표 차이의 절댓값
    dy = abs(y1 - y2)  # y 좌표 차이의 절댓값
    return dx + dy  # 맨하탄 거리

while queue.length() > 0:
    current = queue.pop()

    if current == goal:
        break

    (x, y) = current
    candidates = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    for next in [(h, v) for h, v in candidates if grid[v][h] != 0]:
        new_cost = calc_cost(current, next)
        if next not in came_from or new_cost < cost_so_far[next]:
            queue.push(next, new_cost + heuristic(goal, next))
            cost_so_far[next] = new_cost
            came_from[next] = current

current = goal
path = []
while current is not start:
    path.append(current)
    current = came_from[current]
path.reverse()

print(path)

'''
실행 결과
[(2, 5), (2, 4), (2, 3), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 5), (6, 4), (7, 4), (8, 4), (8, 3), (8, 2), (8, 1)]
'''
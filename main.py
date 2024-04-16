import random
from collections import deque

def generate_random_state():
    colors = ['Red', 'Green', 'Blue']  # representing balls with colors
    pegs = [[], [], []]
    for color in colors:
        peg = random.choice(pegs)
        peg.append(color)
    return pegs

def is_valid_move(current_state, from_peg, to_peg):
    if not current_state[from_peg]:
        return False
    if len(current_state[to_peg]) == 3:  # peg cannot have more than 3 balls
        return False
    return True

def apply_move(current_state, from_peg, to_peg):
    new_state = [list(peg) for peg in current_state]
    ball = new_state[from_peg].pop()
    new_state[to_peg].append(ball)
    return new_state

def bfs_solver(start_state, target_state):
    queue = deque([(start_state, [])])
    visited = set()
    while queue:
        current_state, path = queue.popleft()
        if current_state == target_state:
            return path
        state_tuple = tuple(tuple(sorted(peg)) for peg in current_state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for from_peg in range(3):
            for to_peg in range(3):
                if from_peg != to_peg and is_valid_move(current_state, from_peg, to_peg):
                    new_state = apply_move(current_state, from_peg, to_peg)
                    new_path = path + [(from_peg, to_peg)]
                    queue.append((new_state, new_path))
    return None


start_state = generate_random_state()
target_state = generate_random_state()


solution_path = bfs_solver(start_state, target_state)

print("Start State:", start_state)
print("Target State:", target_state)
print("Solution Path:", solution_path)

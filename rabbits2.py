
start = ['E', 'E', 'E', '_', 'W', 'W', 'W']
goal = ['W', 'W', 'W', '_', 'E', 'E', 'E']


def get_next_states(state):
    moves = []
    pos = state.index('_')
    directions = [-1, -2, 1, 2]
    for d in directions:
        new_pos = pos + d
        if 0 <= new_pos < 7:
            if abs(d) == 1 or (abs(d) == 2 and state[pos + d // 2] != '_'):
                new_state = state[:]
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                moves.append(new_state)
    return moves


def dfs(start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        visited.add(tuple(current))
        for next_state in get_next_states(current):
            if tuple(next_state) not in visited:
                stack.append((next_state, path + [next_state]))
    return None


path = dfs(start, goal)
if path:
    for state in path:
        print(''.join(state))
    print("Steps:", len(path) - 1)
else:
    print("No solution found.")


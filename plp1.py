from collections import deque
from itertools import combinations

# People and their crossing times
people = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

# Initial state:
# Left side has all people, right side is empty, umbrella is on the left, and time is 0
def bfs():
    start_state = (frozenset(people.keys()), frozenset(), 'L', 0)
    queue = deque()
    queue.append((start_state, [start_state]))
    visited = set()

    while queue:
        current, path = queue.popleft()
        left, right, umbrella, elapsed_time = current

        # Success condition
        if len(right) == 4 and elapsed_time <= 60:
            return path

        if (left, right, umbrella) in visited:
            continue
        visited.add((left, right, umbrella))

        if umbrella == 'L':
            # Choose 2 people to go from left to right
            for pair in combinations(left, 2):
                new_left = set(left) - set(pair)
                new_right = set(right).union(pair)
                time = max(people[pair[0]], people[pair[1]])
                new_state = (frozenset(new_left), frozenset(new_right), 'R', elapsed_time + time)
                if new_state[3] <= 60:
                    queue.append((new_state, path + [new_state]))
        else:
            # One person returns from right to left
            for person in right:
                new_right = set(right) - {person}
                new_left = set(left).union({person})
                time = people[person]
                new_state = (frozenset(new_left), frozenset(new_right), 'L', elapsed_time + time)
                if new_state[3] <= 60:
                    queue.append((new_state, path + [new_state]))
    return None

# Run and print result
path = bfs()
if path:
    for step in path:
        left, right, pos, t = step
        print(f"Left: {sorted(left)}, Right: {sorted(right)}, Umbrella: {pos}, Time: {t}")
    print("\nTotal Time:", path[-1][3])
else:
    print("No solution within 60 minutes.")


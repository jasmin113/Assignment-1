from itertools import combinations


people = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}


def dfs():
    start_state = (frozenset(people.keys()), frozenset(), 'L', 0)
    stack = [(start_state, [start_state])]
    visited = set()

    while stack:
        current, path = stack.pop()
        left, right, umbrella, elapsed_time = current

        
        if len(right) == 4 and elapsed_time <= 60:
            return path

        if (left, right, umbrella) in visited:
            continue
        visited.add((left, right, umbrella))

        if umbrella == 'L':
            # Two people cross left to right
            for pair in combinations(left, 2):
                new_left = set(left) - set(pair)
                new_right = set(right).union(pair)
                time = max(people[pair[0]], people[pair[1]])
                new_time = elapsed_time + time
                if new_time <= 60:
                    new_state = (frozenset(new_left), frozenset(new_right), 'R', new_time)
                    stack.append((new_state, path + [new_state]))
        else:
           
            for person in right:
                new_right = set(right) - {person}
                new_left = set(left).union({person})
                time = people[person]
                new_time = elapsed_time + time
                if new_time <= 60:
                    new_state = (frozenset(new_left), frozenset(new_right), 'L', new_time)
                    stack.append((new_state, path + [new_state]))
    return None


path = dfs()
if path:
    for step in path:
        left, right, pos, t = step
        print(f"Left: {sorted(left)}, Right: {sorted(right)}, Umbrella: {pos}, Time: {t}")
    print("\nTotal Time:", path[-1][3])
else:
    print("No solution within 60 minutes.")


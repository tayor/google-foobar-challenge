from itertools import combinations, permutations

def solution(times, time_limit):
    n = len(times)
    shortest = times
    for k in range(n):
        for i in range(n):
            for j in range(n):
                shortest[i][j] = min(shortest[i][j], shortest[i][k] + shortest[k][j])
    for i in range(len(times)):
        if shortest[i][i] < 0:
            return [i for i in range(len(times) - 2)]
    bunnies = range(1, len(times) - 1)
    bunny_sets = []
    for r in range(len(bunnies) + 1):
        for subset in combinations(bunnies, r):
            bunny_sets.append(list(subset))
    bunny_sets.sort(key=len, reverse=True)
    for bunny_set in bunny_sets:
        perm = permutations(bunny_set)
        for subset in perm:
            time = 0
            prev = 0
            for bunny in subset:
                time += shortest[prev][bunny]
                prev = bunny
            time += shortest[prev][-1]
            if time <= time_limit:
                return sorted([bunny - 1 for bunny in subset])
    return []
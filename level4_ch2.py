import math
from collections import defaultdict

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def distance_and_angle_to_point(self_position, point):
    dx, dy = point[0] - self_position[0], point[1] - self_position[1]
    gcd_val = gcd(abs(dx), abs(dy))
    if gcd_val == 0:
        return math.sqrt(dx ** 2 + dy ** 2), (dx, dy)
    return math.sqrt(dx ** 2 + dy ** 2), (dx // gcd_val, dy // gcd_val)

def process_reflected_points(dimensions, your_position, trainer_position, distance, directions):
    max_reflections = max(
        (distance + max(your_position[0], trainer_position[0])) // dimensions[0],
        (distance + max(your_position[1], trainer_position[1])) // dimensions[1]
    )
    for i in range(-max_reflections - 1, max_reflections + 2):
        for j in range(-max_reflections - 1, max_reflections + 2):
            for pos, label in [(your_position, "self"), (trainer_position, "trainer")]:
                reflection = (
                    dimensions[0] * i + pos[0] if i % 2 == 0 else dimensions[0] * (i + 1) - pos[0],
                    dimensions[1] * j + pos[1] if j % 2 == 0 else dimensions[1] * (j + 1) - pos[1]
                )
                if reflection == tuple(your_position):
                    continue
                dist, dir = distance_and_angle_to_point(your_position, reflection)
                if dist < directions[dir][0] or (reflection == tuple(trainer_position) and directions[dir][0] == distance + 1):
                    directions[dir] = [dist, label]

def solution(dimensions, your_position, trainer_position, distance):
    directions = defaultdict(lambda: [distance + 1, ""])
    process_reflected_points(dimensions, your_position, trainer_position, distance, directions)

    count = 0
    for value in directions.values():
        if value[0] <= distance and value[1] == "trainer":
            count += 1

    return count
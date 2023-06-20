def solution(x, y):
    M, F = int(x), int(y)
    generation = 0
    while M != 1 and F != 1:
        if F <= 0 or M <= 0:
            return 'impossible'
        if F > M:
            F, M = M, F
        generation += M // F
        M %= F
    if M < 1 or F < 1:
        return 'impossible'
    generation += max(M, F) - 1
    return str(generation)
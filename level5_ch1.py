def solution(g):
    h, w, s = len(g), len(g[0]), 2 << len(g)
    cnt, n_states = [1] * s, [sum(1 << r if g[r][c] else 0 for r in range(h)) for c in range(w)]
    sp = {i: [] for i in range(s)}
    for i in range(s):
        for j in range(s):
            c = sum((1 << k) for k in range(h) if ((i & (1 << k)) >> k) + ((i & (1 << (k+1))) >> (k+1)) + ((j & (1 << k)) >> k) + ((j & (1 << (k+1))) >> (k+1)) == 1)
            sp[c].append((i, j))
    for i in n_states:
        cnt = [sum(cnt[pred[1]] for pred in sp[i] if pred[0] == j) for j in range(s)]
    return sum(cnt)
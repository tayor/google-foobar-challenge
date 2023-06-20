import numpy as np
from scipy.linalg import inv
from fractions import Fraction

def solution(m):
    m = np.array(m, dtype=np.float64)
    terminal_states = np.where(np.sum(m, axis=1) == 0)[0]

    if len(terminal_states) == 0 or len(m) < 2:
        return [1, 1]
    elif len(terminal_states) == len(m):
        return [1, 1]

    n = len(m)
    for i in range(n):
        row_sum = np.sum(m[i])
        m[i] = m[i] / row_sum if row_sum != 0 else m[i]

    non_terminal_states = np.array([i for i in range(n) if i not in terminal_states])
    sorted_states = np.concatenate((non_terminal_states, terminal_states))
    m = m[:, sorted_states][sorted_states, :]
    n_nt = len(non_terminal_states)

    Q = m[:n_nt, :n_nt]
    R = m[:n_nt, n_nt:]

    F = inv(np.eye(n_nt) - Q)
    FR = np.dot(F, R)

    probs = [Fraction(prob).limit_denominator() for prob in FR[0, :len(terminal_states)]]
    denom = np.lcm.reduce([prob.denominator for prob in probs])
    probs = [int(prob.numerator * denom / prob.denominator) for prob in probs]

    return probs + [int(denom)]

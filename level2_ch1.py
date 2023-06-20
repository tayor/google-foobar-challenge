def solution(l):
    total = sum(l)
    l.sort(reverse=True)
    if total % 3 == 0:
        return int(''.join(map(str, l)))
    else:
        remainders = [[], [], []]
        for i in l:
            remainders[i%3].append(i)
        if total % 3 == 1:
            if remainders[1]:
                remainders[1].sort()
                l.remove(remainders[1][0])
            elif remainders[2] and len(remainders[2]) > 1:
                remainders[2].sort()
                l.remove(remainders[2][0])
                l.remove(remainders[2][1])
            else:
                return 0
        elif total % 3 == 2:
            if remainders[2]:
                remainders[2].sort()
                l.remove(remainders[2][0])
            elif remainders[1] and len(remainders[1]) > 1:
                remainders[1].sort()
                l.remove(remainders[1][0])
                l.remove(remainders[1][1])
            else:
                return 0
        l.sort(reverse=True)
        return int(''.join(map(str, l))) if l else 0

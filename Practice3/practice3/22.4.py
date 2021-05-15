def solve(*coefficients):
    a, b, c = None, None, None
    try:
        if len(coefficients) > 3:
            return None
        c = coefficients[-1]
        b = coefficients[-2]
        a = coefficients[-3]
    except Exception:
        if c is None:
            return None
        if b is None:
            b = 0
        if a is None:
            a = 0
    if a == b == c == 0:
        return ["all"]
    if a == b == 0 != c:
        return []
    if a == 0:
        return [-c / b]
    d = b * b - 4 * a * c
    if d < 0:
        return []
    if d == 0:
        return[(-b + d ** 0.5) / (2 * a)]
    return[(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
print(sorted(solve(1, -3, 2)))

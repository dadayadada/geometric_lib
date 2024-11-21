def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sides do not form a valid triangle")
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("The sides do not form a valid triangle")
    return a + b + c

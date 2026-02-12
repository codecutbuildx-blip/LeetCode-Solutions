def reverseInteger(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign

    res = 0
    while x > 0:
        temp = x % 10
        x //= 10
        res = res * 10 + temp

    return sign * res
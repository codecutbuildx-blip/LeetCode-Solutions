def reverseInteger(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign

    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10

    reversed_num *= sign

    # Check for overflow
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0

    return reversed_num
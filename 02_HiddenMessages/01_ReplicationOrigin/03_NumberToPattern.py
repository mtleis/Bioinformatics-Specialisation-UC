reValues = {0: 'A', 3: 'T', 2: 'G', 1: 'C'}


def NumberToPattern(num, length):
    pattern = ""

    while num > 0:
        div = num // 4
        mod = num % 4
        pattern = reValues[mod] + pattern
        num = div

    while len(pattern) < length:
        pattern = "A" + pattern

    return (pattern)
def modulo11(num: str):
    factor_peso = 2
    sum = 0
    for digit in reversed(str(num)):
        sum += int(digit) * factor_peso
        factor_peso += 1
        if factor_peso > 7:
            factor_peso = 2
    rest = sum % 11
    if rest == 0 or rest == 1:
        return str(0)
    else:
        return str(11 - rest)
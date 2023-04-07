def modulo11(num):
    # Convert the number to a list of digits in reverse order
    digits = [int(d) for d in str(num)][::-1]

    # Calculate the weighted sum of the digits
    sumOfDigits = sum([(i + 2) * d for i, d in enumerate(digits)])

    # Calculate the check digit
    validator = (11 - (sumOfDigits % 11)) % 11

    # Return the check digit as a string
    return str(validator)
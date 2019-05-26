number_raw = input()
number = int (number_raw)


def prime(a):
    checker = 1
    for i in range(2, int(number**0.5+2)):
        if a % i == 0:
            checker = 0
            break

    return checker


factors = []
while number > 1:
    if prime(number) == 1:
        factors.append(number)
        break
    else:
        for i in range(2, int(number**0.5+2)):
            if number % i == 0:
                factors.append(i)
                number = int(number / i)
                break

print(factors)



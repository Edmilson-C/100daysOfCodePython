def add(*args): # args is of type tuple
    sum = 0

    for n in args:
        sum += n

    return sum

print(add(5, 4, 3, 2, 1))

def calculate(**kwargs): #kwargs is of type dictionary
    print(kwargs)
    n = 0
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    n /= kwargs.get("divide")

    return n

print(calculate(add=3, multiply=2, divide=2))
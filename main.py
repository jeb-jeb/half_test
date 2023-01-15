def repeater(func):
    def wrapper(*args, **kwargs):
        for i in range(1, 4):
            print("number of iteration:", i)
            print(func(args, kwargs))
    return wrapper


@repeater
def sum_square(*args, **kwargs):
    result = 0
    all_numbers = []
    for i in args:
        if type(i) == tuple:
            for g in i:
                all_numbers.append(g)
        elif type(i) == dict:
            for g in i.values():
                all_numbers.append(g)

    for i in kwargs.values():
        all_numbers.append(i)

    for num in all_numbers:
        result += pow(num, 2)

    return result


print(sum_square(1, 2, 3, a=2))

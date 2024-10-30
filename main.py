def multiply(a, b):
    if a > b:
        a, b = b, a

    result = a
    for i in range(a, b+1):
        result *= i
    print(result)
if __name__ == '__main__':
    _a = int(input())
    _b = int(input())
    multiply(_a, _b)
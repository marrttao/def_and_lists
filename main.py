def value(number):
    value = 0
    while number > 0:
        number //= 10
        value += 1
    print(value)

if __name__ == '__main__':
    _number = int(input())
    value(_number)
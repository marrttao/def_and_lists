def square(size, symbol, type_of_square):
    if type_of_square:
        for i in range(size):
            print(f"{symbol}  " * size)
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print(f"{symbol}  " * size)
            else:
                print(f"{symbol}  " + "   " * (size - 2) + f"{symbol}  ")


if __name__ == '__main__':
    _size = int(input("Enter the size: "))
    _symbol = input("Enter the symbol: ")[0]
    _type_of_square = input("True False: ").lower() == 'true'
    square(_size, _symbol, _type_of_square)
from collections.abc import Reversible


def extract_digits(number):
    digits = []
    integer_part = int(number)

    while integer_part > 0:
        digits.append(integer_part % 10)
        integer_part //= 10
    digits.reverse()
    fractional_part = number - int(number)
    while fractional_part > 0:
        fractional_part *= 10
        digit = int(fractional_part)
        digits.append(digit)
        fractional_part -= digit
    reversed_digits = digits[::-1] #Сделал двумя способами, чтобы показать, что знаю оба. Ниже закомментирован второй
    # reversed_digits = []
    # for digit in reversed(digits):
    #     reversed_digits.append(digit)
    if reversed_digits == digits:
        return True
    else:
        return False
if __name__ == '__main__':
    number = int(input('Введите число: '))
    extract_digits(number)
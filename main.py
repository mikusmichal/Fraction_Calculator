def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def add(a, b, c, d):
    a = (a * d) + (c * b)
    b = b * d
    nsd = gcd(a, b)
    a = a / nsd
    b = b / nsd
    return a, b


def substract(a, b, c, d):
    a = (a * d) - (c * b)
    b = b * d
    nsd = gcd(a, b)
    a = a / nsd
    b = b / nsd
    return a, b


def multiply(a, b, c, d):
    a = a * c
    b = b * d
    nsd = gcd(a, b)
    a = a / nsd
    b = b / nsd
    return a, b


def divide(a, b, c, d):
    a = a * d
    b = b * c
    nsd = gcd(a, b)
    a = a / nsd
    b = b / nsd
    return a, b


def calc(a, b, c, d, znak):
    if znak == '+':
        a, b = add(a, b, c, d)
    if znak == '-':
        a, b = substract(a, b, c, d)
    if znak == '*':
        a, b = multiply(a, b, c, d)
    if znak == '/':
        a, b = divide(a, b, c, d)
    return a, b


znamenka = ('+', '-', '*', '/')
znamenko = '0'
first_1 = int(input('Zadej citatele:'))
second_1 = int(input('Zadej jmenovatele:'))

if znamenko not in znamenka:
    znamenko = input('Zadej znamenko:')


first_2 = int(input('Zadej citatele:'))
second_2 = int(input('Zadej jmenovatele:'))

first_output, second_output = calc(first_1, second_1, first_2, second_2, znamenko)

print(first_1, '/', second_1, znamenko, first_2, '/', second_2, '=', first_output, '/', second_output)
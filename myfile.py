def armstrong_number(number):
    s=number
    a=len(str(number))
    sum = 0
    
    while number != 0:
        res = number % 10
        sum = sum+(res**a)
        number //= 10

    return s == sum
def armstrong_number(number):
    s=number
    a=len(str(number))
    sum = 0
    while number != 0:
        res = number % 10
        sum = sum+(res**a)
        number //= 10
    return s == sum

if __name__ == "__main__":
    number = "531"
    if armstrong_number(number):
        print("The given number", number, "is an Armstrong number")
    else:
        print("The given number", number, "is not an Armstrong number")
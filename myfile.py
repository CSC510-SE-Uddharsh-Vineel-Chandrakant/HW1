number="531"
s=number
a=len(str(number))
sum=0
while number!=0:
    res = number % 10
    sum = sum+(res**a)
    number = number//10
if s == sum:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
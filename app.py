n = int(input("enter a number: "))
reversed_number = 0

while n != 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n//10
    print('reversed number = ', reversed_number)





#Python program to reverse a number


def reverse(num):
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = (rev * 10) + digit
        num = num //10
    return rev


num = int(input("Enterthe number: "))
res = reverse(num)
print("The reversed number is: ",res)

# In Python, create a program that generates a Fibonacci sequence.

def fibonacci(num):
    n1=0
    n2=1
    print("Fibonacci series are: ",n1,n2,sep='\n')
    for i in range(num-2):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3


num = int(input("Enter the number of values to generate the series: "))
fibonacci(num)

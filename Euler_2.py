#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(n):
    a=1
    b=2
    
    for i in n:
        c=a+b
        a=b
        b=c

for i in range(10):
    print(fibonacci(i))
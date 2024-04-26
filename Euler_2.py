#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Lets start by calculating n fibonacci terms
def fibonacci(n):
    a=1
    b=2
    c=0
    for i in range(n):
        c=a+b
        a=b
        b=c
    
    return c

#Check if it works, its a hair off
for i in range(10):
    print(fibonacci(i))

#Lets try modifying the above to do a single fibonacci to 4 million and sum as it goes
def fibonacci_even_sum():
    
    a=1
    b=2
    c=0
    
    #initialize the sum to 2 so we dont have to consider early edge case
    even_sum=2
    while c < 4_000_000:
        c=a+b
        a=b
        b=c
        
        if c % 2 == 0:
            even_sum+=c
    return even_sum

answer=fibonacci_even_sum()
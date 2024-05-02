#Find the sum of all primes below two million.

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

pSum=0
for num in range(2_000_000):
    
    primeFlag=is_prime(num)
    
    if primeFlag==True:
        pSum+=num
# -*- coding: utf-8 -*-
# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
    # for i in range(2, int(num)):

        if num % i == 0:
            return False
    return True

num=0
c=0
while c!= 10001:
    
    num+=1
    primeFlag=is_prime(num)
    
    if primeFlag==True:
        c+=1
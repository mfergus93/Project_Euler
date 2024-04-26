#What is the largest prime factor of the number 600851475143?

#Lets just extract all primes of a number grossly and see from there:

def primes(n):
    
    for i in range(n):
        if n % i == 0:
            divisor=i
            
            prime_flag=1
            for j in range(divisor):
                
                if j == 1:
                    continue
                
                if divisor % j == 0:
                    prime_flag=0
            
            if prime_flag == 1:
                prime_list.append([divisor])
                
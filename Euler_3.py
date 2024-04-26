#What is the largest prime factor of the number 600851475143?

#Lets just extract all primes of a number grossly and see from there:

def primes(n):
    
    prime_list=[]
    for i in range(1,n):
        if n % i == 0:
            divisor=i
            
            prime_flag=1
            for j in range(2,divisor):
                
                if j == 1:
                    continue
                
                if divisor % j == 0:
                    prime_flag=0
            
            if prime_flag == 1:
                prime_list.append([divisor])
    return prime_list

#test=primes(68)

#This takes forever
answer=primes(600851475143)


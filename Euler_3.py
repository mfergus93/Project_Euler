#What is the largest prime factor of the number 600851475143?

#Lets just extract all primes of a number grossly and see from there:

n=600_851_475_143
prime_list=[]
for num in range(1,n//2+1):
    if n % num == 0: #if the remainder is zero
    #     divisor=i #it is a divisor
        prime_flag=1 #assume its prime and test to falsify
        
        for prime in prime_list: #for each prime discovered so far
            if prime == 1:
                continue
            
            if num % prime == 0: #is this number divisible by any prime
                prime_flag=0
        
        if prime_flag == 1:
            prime_list.append(num)
        
    if num % 10000 == 0:
        print(num)

115560000
# def primes(n):
    
#     prime_list=[]
    
#     for i in range(1,n//2+1): #for each natural number between 1 and n//2
        
#         if n % i == 0: #if the remainder is zero
#             divisor=i #it is a divisor
            
#             prime_flag=1 #assume its prime and test to falsify
            
#             for j in range(2,divisor//2): #for each natural number from 2 to half divisor-1
#                 if j == 1:
#                     continue
                
#                 if divisor % j == 0: #is this number divisible by any number
#                     prime_flag=0
            
#             if prime_flag == 1:
#                 prime_list.append(divisor)
#     return prime_list

# # test=primes(10)

# #This takes forever
# answer=primes(600851475143)


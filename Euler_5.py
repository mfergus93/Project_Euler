#What is the smallest psotive number that is evenly divisible by all of the numbers from 1 to 20?

#just a guess here
import math
smallestPostiveNumber=math.factorial(20)
#well it has cofactors since 20 is divisible by 2??

#LCM between 2 and 20 then? whats that for a range??

#ok brute approach
def getSmallestPositiveNumber(n):
    i=20
    c=1
    while c==1:
        
        div_flag=True
        for j in range(2,n+1):
            
            if i % j !=0:
                div_flag=False
                continue
        
        if div_flag==True:
            return i
        i=i+1

answer=getSmallestPositiveNumber(20)

#takes 5 minutes to run, probably a method using least common multiple of 1 to 20

#What is the value of the first triangle number to have over five hundred divisors?

def triangle_number_divisor_count():

    c=1
    factors=1
    while c==1:
        divisor_count=0
        
        triangleNumber=0
        for i in range(1,factors+1):
            triangleNumber+=i
    
        for i in range(1,triangleNumber):
            if triangleNumber % i ==0:
                divisor_count+=1
        if divisor_count==500:
            return triangleNumber
        factors+=factors

answer=triangle_number_divisor_count()
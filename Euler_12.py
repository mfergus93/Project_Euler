#What is the value of the first triangle number to have over five hundred divisors?

#so this is pretty brute force, perhaps theres a better way
def triangle_number_divisor_count(n):

    c=1
    i=1
    triangleNumber=0
    
    while c==1:
        
        divisor_count=0
        triangleNumber+=i
        for j in range(1,triangleNumber+1):
            if triangleNumber % j == 0:
                divisor_count+=1
        if divisor_count>=n:
            c=0
            return triangleNumber
        i+=1

answer=triangle_number_divisor_count(500)
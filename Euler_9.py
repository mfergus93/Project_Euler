#There exists exactly one Pythagorean triplet for which a+b+c=1000. Find a*b*c
import math

def pythagoreanTriplet():
    for a in range(1,1000):
        
        for b in range(1,1000):
            
            c = math.sqrt(a*a+b*b)
            if a+b+c==1000:
                
                return a,b,c


a, b, c=pythagoreanTriplet()
answer=int(a*b*c)
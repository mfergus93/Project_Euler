#Find the sum of all multiples of 3 or 5 below 1000.

#Iterative approach
sum=0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum+=i

#Direct approach
def func(n):
    c=1
    sum=0
    while n*c < 1000:
        sum+=n*c
        c+=1
    return sum

sum2=func(3)+func(5)-func(15)
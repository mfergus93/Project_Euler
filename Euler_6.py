#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

sumSquare=0
squareSum=0

for i in range(1,101):
    sumSquare+=i*i
    print(i)

for i in range(1,101):
    squareSum+=i
    #sum is a reserved word...

squareSum=squareSum*squareSum

answer=squareSum-sumSquare
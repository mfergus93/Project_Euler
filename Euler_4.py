#Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome_test(n):
    
    n=str(n)
    i=0
    j=-1
    c=1
    palindrome_flag=True
    
    while c==1:
        L= n[i]
        R = n[j]
        
        if L!=R:
            c=0
            palindrome_flag=False
        if L==R:
            i=i+1
            j=j-1
        
        if len(n)+j-i<2:
            c=0
            #we could just return here surely?
    
    return palindrome_flag

for i in range(100, 1000):
    for j in range(100, 1000):
        
        palindromeCandidate=i*j
        palindrome_flag=palindrome_test(i*j)
        
        if palindrome_flag==True:
            largest_palindrome=palindromeCandidate
            int1=i
            int2=j

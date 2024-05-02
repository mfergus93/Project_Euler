#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?


def num_length(num):

    single=['one','two','three','four','five','six','seven','eight','nine']
    teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen',\
        'eighteen','nineteen']
    double=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
    triple=['hundredand']
    quad=['thousand']
    
    string=[]
    
    for i in str(num):
        
        if len(num)==1:
            string+=len(single[num-1])

        
        if len(num)==2 and num<=20:
            string+=len(teens[num-10])
        
        if len(num)==2 and num>=20:
            string+=len(double[num//10-2])
        
        if len(num)==3 and num
            string+=len(triple[0])
            
        if len(num)==4:
            return len("one thousand")
        
    return string


numLength=0
for i in range(1,1001):
    numLength+=num_length(num)
    
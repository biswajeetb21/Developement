t= int(input())

while t>0:
    t -=1
    n = int(input())
    digit= 0
    rev = 0
    while n>0:
        digit = n%10
        rev= rev*10+digit
        n = n//10
    print(rev)
     

import random
a = random.randint(1,100) 
b = int(input("Enter the numer to guess in between 1 to 100 : "))
x=1
while(a!=b):
    x=x+1
    if(a>b):
        print("The number ",b," is small : ")
    elif(a<b):
        print("The number ",b," is big : ")
    b = int(input("Enter the numer again : "))
    
else :
    print("The Number is ",a ,"\n You have complete it in step of",x)
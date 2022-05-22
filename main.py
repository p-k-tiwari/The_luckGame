import random
l = [1,2,3,4,5,6,7,8,9,10]
b= random.choice(l)
while(True):
     a= int(input("enter the number between 1 to 10"))
     if(a>b):
        print("small number please🙃", end=" ");
        print("try again⬇️");
     elif(a<b):
        print("😅Greater number please");
        print("TRY AGAIN⬆️");
     else:
        print("💯Correct guess💯");
        break;        

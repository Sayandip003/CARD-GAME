print(" A = Ace \n H = Heart \n S = Spades \n D = Diamonds")
y=input("Enter your card type (A/S/H/D)")
x=int(input("Enter your card number (1-10)"))
import random
n = random.randint(0,10)
import string  
def specific_string(length):  
    sample_string = 'ASHD' 
    r = ''.join((random.choice(sample_string)) for x in range(length))  
    print("Card entered by Computer is ",r ,n)  
specific_string(1)
if(x>10):    
    print("Card no. is invalid")    
elif(y!='A' and y!='S' and y!='H' and y!='D'):    
    print("Wrong card type")    
elif(y=='A' and x==n):
    print("You Win ")
elif(y=='S' and x==n):
    print("You Win ")
elif(y=='H' and x==n):
    print("You Win ")
elif(y=='D' and x==n):
    print("You Win ")      
else:
    print("Computer wins, you lose")
    

    
    
    


import random


print('Welcome to Dice Rolling Simulator')

res = 'Y'
while res == "Y" or res == "YES" or res == "y" or res == "yes" or res == "Yes": 
    print('You Rolled :')
    print(random.randint(1,6))
    res= raw_input('Want to play again?  Y or N :')

print('Thanks for Playing')
    
        
   

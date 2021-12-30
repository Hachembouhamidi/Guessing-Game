import random

print("Welcome Dear Player")
print("this game contains 3 difficulties")
print("1-easy")
print("2-Medium")
print("3-Hard")
count =0
difficulty = input("please choose you difficulty ")
upper = 0
lower = 0
if(difficulty.capitalize() == "Easy"):
       upper = 100
elif(difficulty.capitalize()=="Medium"):
      upper = 1000
elif(difficulty.capitalize() =="Hard"):
      upper = 10000

      
number = random.randint(lower,upper) 

print("the game has started")
playerinput=int(input("Try to guess the number !! : "))
while playerinput != number:
    if playerinput<number:
        playerinput=int(input("too low try again : "))
        count+=1
    elif playerinput>number:
        playerinput=int(input("too high try again : "))
        count+=1






if count == 0 :
  print("yay you did it!! the number was {} , you are a genius for one shoting it".format(number))
else:
  score = upper/count
  print("yay you did!! it the number was {} it only took you {} guesses".format(number,count))

    
    
    
    

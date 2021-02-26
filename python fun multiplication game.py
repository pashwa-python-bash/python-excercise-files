import time
import random

start = input("Do you want to play the multiplication game:  (yes/no):  ").lower()

if start == "yes":
  correct = 0
  questions = 0

  delay = int(input("\nHow long do you want to answer as many questions as you can(type ur answer in seconds):  "))
  end = time.time() + delay

  



  while time.time() < end:
      n1 = random.randint(2,12)
      n2 = random.randint(2,12)
 
      answer  = int(input(str(n1) +  "x" + str(n2) + "=  "))
      questions +=1
    
      if answer == n1 * n2:
        correct +=1
        print("Correct!")

      
      
      else:
        print("Incorrect!")

  print("\nTime's up!")
  time.sleep(2)
  print(f"\nYou got {correct} correct out of {questions} questions.")
  
elif start == "no":
  print("Thanks for coming anyways!")
else:
  print("Invalid Option!")
  

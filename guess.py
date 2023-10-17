import random
random_number = random.randint(1,100)
i=0
while True:
   while True:
      guess= int(input("Enter value "))
      i+=1
      if guess>random_number:
      	print("Your guess is high ")
      elif guess<random_number:
      	print("Your guess is low ")
      else:
          print(f"Hurray you are correct after " + str(i) + " trials")
          break
print("Thanks for playing this game")  

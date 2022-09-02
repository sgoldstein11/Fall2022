import random

stones = 12;
while (stones >0):
  stonesTaken = input("How many stones would you like to take? (Choose 1,2 or 3 only)")
  print("You have taken " + stonesTaken + " stones")
  stonesTaken = int(stonesTaken)
  stones = stones - stonesTaken
  stones = str(stones)
  print (stones + " stones are left")
  stones = int(stones)
  if stones == 0:
    print("You took the last stone.You win!")
  elif stones >3:
    stonesTaken = random.randint(1,4)
    print("The computer has taken " + str(stonesTaken) + " stones")
    # print(stonesTaken)
    # print("stones")
    stones = stones - stonesTaken
    print("There are " + str(stones) + " left in the pot")
    # print(stones)
    # print("left in the pot")

  else:
 
   stones = stones - stonesTaken
   print("The machine took " + str(stonesTaken) + ". There are " + str(stones)+ " left")
  

  if stones <=0:
    print("The machine took the last stone. You lost!")

      
  stones= int(stones)

#print("You have no more stones")
   
#need to add in random number generator to play against computer 
#need else/if 

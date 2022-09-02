import random

stones = 12
while (int(stones) >0):
  stonesTakenHuman = input("How many stones would you like to take? (Choose 1,2 or 3 only)")
  print("You have taken " + stonesTakenHuman + " stones")
  stones -= int(stonesTakenHuman)
  print("There are " + str(stones) + " left")
  if (int(stones)==0):
    print("You win! You took the last stone")
    break
  stonesTakenComp = random.randint(1,3)
  print("The computer has taken " +           
  str(stonesTakenComp) + " stones")
  stones -= stonesTakenComp
  print (str(stones) + " stones are left")       
  if(int(stones) <=0):
    print("Sorry the computer won :(")
    break

  

   # elif stones >3:
  
  #   # print(stonesTaken)
  #   # print("stones")
  #   stones = stones - stonesTakenComp
  #   print("There are " + str(stones) + " left in the pot")
  #   # print(stones)
  #   # print("left in the pot")

  # else:
 
  #  stones = stones - stonesTaken
  #  print("The machine took " + str(stonesTaken) + ". There are " + str(stones)+ " left") 

      
  

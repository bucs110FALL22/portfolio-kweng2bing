import random
rnum = random.randrange(1,11)
tries = 0
print(rnum)
while (tries < 3 and tries >= 0):
    num = int(input("Guess a number form 1 to 10"))
    if num == rnum:
      print("Your correct")
      tries = -1
      chance = tries
    elif num > rnum:
      print( str(num), "is too high. Guess a lower number")
      tries = tries + 1
    elif num < rnum:
      print(str(num), "is too low. Guess a higher number")
      tries= tries + 1
if tries == 3:
  print("Better luck next time")


# chance = 3
# for i in range(chance):
#   if tries == 3: 
#     print("Sorry to many tries")
#     tries = 3
#   else: 
#     num = int(input("Guess a number form 1 to 10"))
#     if num == rnum:
#       print("Your correct")
#       chance = tries
#     elif num > rnum:
#       print( str(num), "is too high. Guess a lower number")
#       tries = tries + 1
#     elif num < rnum:
#       print(str(num), "is too low. Guess a higher number")
#       tries= tries + 1

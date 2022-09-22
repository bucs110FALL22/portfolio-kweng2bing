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

# num = random.randrange(1,11)
# num_guesses = 0
# for i in range(chance):
#   guess_num = int(input("Guess a number form 1 to 10"))
#   num_guesses += 1
#   if guess_num > num:
#     print("your guess is to high")
#   elif guess_num < num:
#     print("your guess is too low")
#   else:
#     print("Correct")
#     break
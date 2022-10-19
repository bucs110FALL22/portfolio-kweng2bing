def percentage_to_letter(score=0):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >=60:
        return "D"
    elif score >= 50:
        return "F"

def is_passing(letter=None):
    if letter in "ABC":
        return True
    else:
        return False
# You have to evaluate seperately  Cannot do if letter == "A" or "B" or "C":
# Solution 1  if letter == "A" or letter == "B" or letter == "C":
# Solution 2 if letter in "ABC": 
# Solution 3 return letter in "ABC"
score = int(input("Score?"))
letter =percentage_to_letter(score)
passing = is_passing(letter)
print(score, letter, passing)
# while testing code, try to test cases that shouldn't work 
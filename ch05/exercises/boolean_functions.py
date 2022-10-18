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
    if letter == "A" or "B" or "C":
        return True
    else:
        return False

score = int(input("Score?"))
letter =percentage_to_letter(score)
passing = is_passing(letter)
print(score, letter, passing)
number1= int(input("Number 1?")) 
number2= int(input("Number 2?"))

def multiply(num1, num2):
  number= 0
  for i in range(num2):
    number+= num1
  print(f"Multiply result: {number}")

multiply(number1, number2)

def exponent(num1, num2):
  number = 1
  for i in range(num2):
    number*= num1
  print(f"Exponenet Result:{number}")

exponent(number1, number2)

def square(num1):
  number = num1* num1
  print(f"Square Result:{number}")
square(number1)
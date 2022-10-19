def multiply(num1, num2):
  number= 0
  for i in range(num2):
    number+= num1
  return number

def exponent(num1, num2):
  number = 1
  for i in range(num2):
    number*= num1
  return number 

def square(num1):
  return multiply(num1, num1)

def main():
  numberone = int(input("Number 1?"))
  numbertwo = int(input("Number 2?"))
  result = multiply(numberone, numbertwo)
  print(result)
  print("===")
  result = exponent(numberone, numbertwo)
  print(result)
  print("===")
  result = square(numberone)
  print(result)

main()

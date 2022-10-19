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
  result = (multiply(numberone, numbertwo), exponent(numberone, numbertwo), square(numberone))
  print(f"Multiply:{result[0]}, Exponent:{result[1]}, Square of number 1: {result[2]}")
 
main()

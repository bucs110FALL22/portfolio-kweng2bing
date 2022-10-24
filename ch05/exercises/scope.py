def multiply(num1, num2):
  number= 0
  if num2 >= 0:
    for i in range(num2):
      number+= num1
    print(number)
  if num2 < 0:
    for i in range(abs(num2)):
      number+= num1
  return number

def exponent(num1, num2):
  number = 1
  if num1 > 0:
    for i in range(abs(num2)):
      number*= num1
    if num2 > 0:
      return number 
    elif num2 < 0:
      return 1/number
  elif num1 < 0:
    for i in range(abs(num2)):
      number*= num1
    if num2 > 0:
      return number
    if num2 < 0:
      return 1 / number
 
def square(num1):
    return abs(multiply(num1, num1))

def main(numberone, numbertwo):
  # numberone = int(input("Number 1?"))
  # numbertwo = int(input("Number 2?"))
  result = (multiply(numberone, numbertwo), exponent(numberone, numbertwo), square(numberone))
  print(f"Multiply:{result[0]}, Exponent:{result[1]}, Square of number {numberone} is: {result[2]}")

main(-6,1)

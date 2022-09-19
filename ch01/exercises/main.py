print("hello")

# Part 1
a= 10 * 5
# 50
b= 10 ** 2
# 100
c= 15 / 10
# 1.5
d= 15 // 10
# 1
e= -15 // 10
# -2
f= 15 % 10
# 5
g= 10 % 15
# 6
h= 10 % 10
# 0
i= 0 % 10
# 0
j= 10 / 15
# 0.6
# Answer should be repeating but the deicmal is finite
print(a,b,c,d,e,f,g,h,i,j)
print(type(j))

# Part 2
rate = float(input("What is the current exhcange rate from Euro to USD?"))
amount  = float(input("How much Euro do you want to convert to USD?"))
total= rate*amount
result= str(total-3)
print("$ " + result + " will be given back to you! Thank you for your service!")
# print(result)


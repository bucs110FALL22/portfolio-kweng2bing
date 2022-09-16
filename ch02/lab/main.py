import random


#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week, type(cost_per_week))


classes_per_week = 3
print("Classes per week ", classes_per_week ,type(classes_per_week))

cost_per_class = int(cost_per_week // classes_per_week)
print("Everyday, you're paying $"+ str(cost_per_class) +" for each of your classes! Thank you for your service!",type(cost_per_class))

#Part B
random.randrange(1,6)

myList = ["phone", "4" , 0.5, "CS110", 0, "food"]
print(myList)
myRandom =  random.choice(myList)
print("Random thing from the list: " + str(myRandom), type(myRandom))

# Loop to get multiple output
# numberOfOutput = int(input("How many random output do you want?"))
# for i in range(numberOfOutput):
#   myRandom =  random.choice(myList)
#   print("Random list" + str(myRandom), type(myRandom))



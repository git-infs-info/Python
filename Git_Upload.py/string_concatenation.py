#Ask user for name
name = input("What is your name?: ")

#Ask user for age
age = input("What is your age?: ")

#Ask user for city
city = input("What city do you live in?: ")

#Ask user what they enjoy doing
enjoy = input("What do you enjoy doing?: ")

#Ask user what is todays date
date = input("What is todays date?: ")

#Create output text
string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}. Todays date is {}, thank you for your input today! "
output = string.format(name, age, city, enjoy, date)

#Print output to screen
print(output)



make = input("What is the make of your car?: ").strip().capitalize()
model = input("What is the model of your car?: ").strip().capitalize()
year = input("What year is your car?: ").strip()
color = input("What color is your car?: ").strip().capitalize()
output = "Thank you for registering your car with us. We have registered your {}, {}, {}, {}, in our system. Have a nice day!".format(year,color,make,model)
print(output)

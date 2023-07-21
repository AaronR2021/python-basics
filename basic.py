print("Hello World")
print(1 + 2)
# comment is "#"
# Python is a dynamically typed language. 
# datatype it set at runtime
varable = 4+6
varable+=2
print(varable)

#imported data 
# titanic_data = pd.read_csv("../input/titanic/train.csv")
# const ageSum = (titanic_data.age<20).sum()

#Fuctions
def add_three(inputVar):
    output_var = inputVar+3
    return output_var
# 4 spaces between border and body

print(add_three(2))
print(type (add_three(3)))
#convert to int
print(int(-1.023))
# its False not false
print("abc"*True)

#if statement
if 100 > 38:
    message = "its true!"
    print(message)

# if in function
def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "true!"
    return message

#if else
def evaluate_temp_with_else(temp):
#<- remeber the i/ else ends in ":"
    if temp > 38:
        message = "Fever!"
    else: 
        message = "Normal temperature."
    return message

# if elif else
def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

# base Idea
# TODO: Edit the function to return the correct grade for different scores
def get_grade(score):
    if score<=100 and score>=90:
        grade = "A"
    elif score<=89 and score>=80:
        grade = "B"
    elif score<=79 and score>=70:
        grade = "C"
    elif score<=69 and score>=60:
        grade = "D"
    else:
        grade = "F"
    return grade

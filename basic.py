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


flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

# first 3 entires
print("First three entries:", flowers_list[:3])
# final 2 entries
print("Final two entries:", flowers_list[-2:])

#remove
flowers_list.remove("globe thistle")
print(flowers_list)
#add
flowers_list.append("snapdragon")
print(flowers_list)

hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
print("Total books sold in one week:", sum(hardcover_sales))
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(flowers.split(","))
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
print(alphabet.split('.'))
# condition each element
test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings] # [condition for i in arrayname]
print(test_liked) #[true, true, true, false, false]
# use sum to get the count of positives
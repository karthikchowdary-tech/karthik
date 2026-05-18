# if statement
# The simplest conditional checks whether something is true
age = 18
if age >= 18:
    print("You are an adult")


    # if else
    # Use this when you want two possible outcomes
    age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


    # if elif else statement
   # Use this when there are multiple conditions
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

    #nested if else
if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")

    # match case
    
    number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")
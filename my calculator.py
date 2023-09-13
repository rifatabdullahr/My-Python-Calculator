#for add 2 numbers
def add(x,y):
    return x + y

#for substraction
def substraction(x,y):
    return x - y

#for multiplication
def multi(x,y):
    return x * y

#for division
def division(x,y):
    if y == 0:
        return "Error! Can not divide by 0"
    return x / y

#enter user's name
print("*!*!*!     Greetings     *!*!*!")
name = input("What is your name?\n: ")
print("'Welcome to " +name+"'s" + " Calculator'\n\n\n")
print("What do you want to calculate?")
print("1.Sum")
print("2.Substraction")
print("3.Multiplication")
print("4.Division \n")

while True:
    
    #take user's choice    
    choice = input("Your Choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):

        try :
            number1 = float(input("Enter First Number: "))
            number2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input.Pleas Enter a number")
            continue
            
        if choice == '1':
            print(number1, "+", number2, "=", add(number1, number2) )
        elif choice == '2':
            print(number1, "-", number2, "=", substraction(number1, number2) )
        elif choice == '3':
            print(number1, "*", number2, "=", multi(number1, number2) )
        elif choice == '4':
            print(number1, "/", number2, "=", division(number1, number2) )
         #check if user want another calculation
         #break while loop if ans is no
        while True:
            next_calculation = input("Let's do another calculation? (yes/no)\n: ")
            if next_calculation.lower() in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if next_calculation.lower() != "yes":
            break
            
    else:
        print("Invalid Input.Pleas select option 1/2/3/4")        
print("Thank You! for calculating in ", name, "'s Calculator.Have a Nice Day!")

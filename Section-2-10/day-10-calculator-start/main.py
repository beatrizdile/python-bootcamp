#Calculator
from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def sub(n1, n2):
    return n1 - n2

#Multiply
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

ope = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    
    print("")
    
    for i in ope:
        print(i)
    
    ope_chosen = input("\nPick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    function = ope[ope_chosen]
    result = function(num1, num2)
    
    print(f"\n{num1} {ope_chosen} {num2} = {result}")
    current_result = result
    
    while(True):
        continue_num = input(f"\nType 'y' to continue calculating with {current_result}, or type 'n' to start a new calculation: ")
        if continue_num == "n":
            calculator()
        elif continue_num != "y":
            print("Invalid answer.")
            continue
    
        ope_chosen_2 = input("\nPick another operation: ")
        num3 = float(input("What's the next number?: "))
        
        function_2 = ope[ope_chosen_2]
        result_2 = function_2(result, num3)
        current_result = result_2
        
        print(f"\n{result} {ope_chosen_2} {num3} = {result_2}")

calculator()
import re
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print("--- Bolads Calculator ---")
    print("You can continue equations after the result.")
    print("If you digit anything different to equations, not be considered.")
    print("Type 'new' to new equation.")
    print("Type 'quit' to exit.\n")

run = previous = cond = True

def perform_math():
    global run
    global previous
    global cond
    
    equation = ''

    if cond:
        equation = input("Enter equation: ")
    else:
        print("Result: ", end='')
        equation = input(str(previous))

    if equation.lower() == "quit":
        print("\nGoodbye, human.")
        time.sleep(1.5)
        run = False
    elif equation.lower() == "new":
        cls()
        cond = True
    else:
        equation = re.sub('[a-zA-Z,:()" "]', '', equation)
        if cond:
            previous = eval(equation)
            cond = False
        else:
            previous = eval(str(previous) + equation)

cls()

while run:
    perform_math()
import re
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print("--- Bolads Calculator ---")
    print("You can continue equations after the result.")
    print("If you digit anything different to equations, not be considered.")
    print("Type 'help' to help.")
    print("Type 'new' to new equation.")
    print("Type 'quit' to exit.\n")

run = previous = cond = run_help = True

def help():
    global run_help

    print("A little information for you!")
    print("You can use these operations (including all together):\n")
    print("'+' to add.")
    print("'-' to subtract.")
    print("'*' to multiply.")
    print("'/' to divide.")
    print("'**' for exponential.")
    print("'//' for a floor division.")
    print("'%' returns the rest of division.\n")
    back = input("If you understood, type 'back' for back to equations.\n\n")

    if back.lower() == 'back':
        run_help = False

def perform_math():
    global run
    global run_help
    global previous
    global cond

    equation = ''

    if cond:
        equation = input("Enter equation: ")
    else:
        print("Result: ", end='')
        equation = input(str(previous) + " ")

    if equation.lower() == "quit":
        print("\nGoodbye, human.")
        time.sleep(1)
        run = False
    elif equation.lower() == "new":
        cls()
        cond = True
    elif equation.lower() == "help":
        cls()
        run_help = True
        while run_help:
            help()
            cls()
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

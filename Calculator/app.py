""" Calculator
----------------------------------------
"""
def addition ():
    print("Addition")
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def subtraction ():
    print("Subtraction");
    n = float(input("Enter the number: "))
    t = 0 
    sum = 0
    while n != 0:
        ans = ans - n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def multiplication ():
    print("Multiplication")
    n = float(input("Enter the number: "))
    t = 0
    ans = 1
    while n != 0:
        ans = ans * n
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    return [ans,t]
def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    return [ans,t]

while True:
    list = []
    print(" My first python program!")
    print(" Simple Calculator in python by Patel Jay")
    print(" Enter 'a' for addition")
    print(" Enter 's' for subtraction")
    print(" Enter 'm' for multiplication")
    print(" Enter 'v' for average")
    print(" Enter 'q' for quit")
    c = input(" ")
    if c != 'q':
        if c == 'a':
            list = addition()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 's':
            list = subtraction()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'm':
            list = multiplication()
            print("Ans = ", list[0], " total inputs ",list[1])
        elif c == 'v':
            list = average()
            print("Ans = ", list[0], " total inputs ",list[1])
        else:
            print ("Sorry, Invalid Character")
    else:
        break

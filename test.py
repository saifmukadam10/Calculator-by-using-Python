from random import choice


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
"-":subtract,
"*":multiply,
"/":divide,
}

def calculator():
    should_accumalate= True
    n1=float(input("whats your first number: "))

    while should_accumalate:
     for symbol in operations:
        print(symbol)
    operations_symbol = input("choose operation")
    n2=float(input("whats your second number: "))

    answer = (operations[operations_symbol](n1,n2))
    print(f"{n1} {operations_symbol} {n2} = {answer}")

    choice=input("If you wish to continue press 'Y',or else type 'n' to start a new calculation")

    if choice=='Y':
        n1=answer

    else:
        should_accumalate=False
        print("\n"*20)
        calculator()


calculator()
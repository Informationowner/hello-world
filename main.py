import random

answer = input("Would you like to start?(Y or N) ====>   ")
answer.lower()

while answer != 'y' and answer != 'n':
    answer = input("Wrong! Please, input correct answer    ")

while answer == "y":
    x = random.randint(1,6)
    print(x)
    if x == 1:
        print("*")
    elif x == 2:
        print("* *")
    elif x == 3:
        print("*\n" 
              " *\n"
              "  *")
    elif x == 4:
        print("* *\n"
              "* *")
    elif x == 5:
        print("* *\n"
              " *\n"
              "* *")
    else:
        print("* *\n"
              "* *\n"
              "* *")
    answer = input("\nAgain? =====>     ").lower()

    while answer != 'y' and answer != 'n':
        answer = input("Wrong! Please, input correct answer    ")

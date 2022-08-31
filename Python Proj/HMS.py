# Health Management System
import datetime



def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Ali-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Ali-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Wali-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Wali-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("Hozaifa-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif c == 2:
            value = input("type here\n")
            with open("Hozaifa-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Ali),2(Wali),3(Hozaifa)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Ali-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Ali-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Wali-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Wali-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("Hozaifa-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Hozaifa-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Ali,Wali,Hozaifa)")


print("Welcome to Health Management System: ")
a = int(input("Press 1 for Input the value and 2 for Output: "))

if a == 1:
    b = int(input("Press 1 for Ali 2 for Wali 3 for Hozaifa "))
    take(b)
else:
    b = int(input("Press 1 for Ali 2 for Wali 3 for Hozaifa "))
    retrieve(b)
    
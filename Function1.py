# FUnction Which accepts nothing and retun nothing
from ast import Mult
from audioop import mul
from tkinter import MULTIPLE


def Demo1():
    print("Inside Demo1")

# Function accepts one parameter and returns nothing
def Demo2(No):
    print("Insdie Demo2 with argument : ",No)

# FUnction accepts one parameter and return one parameter
def Demo3(No):
    print("Inside Demo3 with argument",No)
    return No+No

#Function Accepts 2 parameter and return one parameter
def Demo4(No1,No2):
    print("Inside Demo4")
    Add = No1 + No2
    return Add

#Function Accepts 2 parameter and return two parameter
def Demo5(No1,No2):
    print("Inside Demo5")
    Add = No1 + No2
    Sub = No1 - No2
    MULTIPLE = No1 * No2
    return Add,Sub,MULTIPLE

def main():
    Demo1()
    Demo2("Hello")
    Ans = Demo3(105)
    print("Return value of Demo3 is :",Ans)
    Ans = Demo4(10,11)
    print("Retrun value is :",Ans)

    Ans1,Ans2,Ans3 = Demo5(11,10)
    print("First return value : ",Ans1)
    print("Second return value: ",Ans2)
    print("Third return value :",Ans3)


if __name__ == "__main__":
    main()

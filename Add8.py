print("Application to demonstrate Industrial Programming")

import MarvellousModule
    
def main():
    print("Value of __name__ from main is : ",__name__)
    print("Enter First Number :")
    no1 = int(input())
    print("Enter Second Number:")
    no2 = int(input())

    Sum = MarvellousModule.Addition(no1,no2)
  
    print("Addition is :",Sum)

if __name__ == "__main__":
    main()

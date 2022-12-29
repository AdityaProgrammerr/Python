import time

def DisplayEven(No):
    for i in range(No):
        if(i % 2 == 0):
            print("Even Number :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd Number :",i)


def main():
    print("Demonstration if serial programming")
    DisplayEven(2000)
    DisplayOdd(2000)

if __name__ =="__main__":
    main()
    start_time = time. process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)


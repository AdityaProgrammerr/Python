import time
import multiprocessing

def DisplayEven(No):
    for i in range(No):
        if(i % 2 == 0):
            print("Even Number :",i)


def DisplayOdd(No):
    for i in range(1,No,1):
        if(i % 2 != 0):
            print("Odd Number :",i)


def main():
    print("Demonstration if Parallel programming using multiple processess")
    Number = 200

    p1 = multiprocessing.Process(target = DisplayEven, args = (Number,))
    p2 = multiprocessing.Process(target = DisplayOdd,args = (Number,))

    p1.start()
    p2.start()

    print("End of main")

if __name__ =="__main__":
    main()
    start_time = time.time()
    main()
    end_time = time.time()
    print("Execution time is : ",end_time - start_time)
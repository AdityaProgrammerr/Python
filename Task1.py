import schedule
import time
import datetime

def Task_Minute():
    print("Task based on minutes scheduled at : ",datetime.datetime.now())

def Task_Hour():
    print("Task based on Hour scheduled at : ",datetime.datetime.now())

def Task_Day():
    print("Task based on Day scheduled at : ",datetime.datetime.now())



def main():
    print("Inside task schedular")
    print("Current time is : ",datetime.datetime.now())

    schedule.every(1).minutes.do(Task_Minute)
    schedule.every(1).hour.do(Task_Hour)
    schedule.every().saturday.at("20:35").do(Task_Day)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
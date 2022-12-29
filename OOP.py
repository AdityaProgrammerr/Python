#Accept 2 number and perform addition and substraction of of it

# Class = Characteristics + Behaviours
# Class = Data + Function 


class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2
        


def main():
    print("Enter first number")
    No1 = int(input())

    print("Enter second number")
    No2 = int(input())


if __name__ == "__main__":
    main()

def Area(Radius,PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def main():
    RValue = 10.5
    PIValue = 3.14

    # Positional Argument
    Ans = Area(RValue,PIValue)
    print("Area of circle is : ",Ans)
   # Keyword Argument

    Ans = Area(PI = PIValue,Radius = RValue)
    print("Area of circle is : ",Ans)

     # Positional argument and Second is default
    Ans = Area(10.5)
    print("Area of circle is : ",Ans)

    # Keyword argument and second is default
    Ans = Area(Radius = 10.5)
    print("Area of circle is : ",Ans)
    
    # Keyword arguements
    Ans = Area(PI = 7.10,Radius = 10.5)
    print("Area of circle is : ",Ans)

if __name__ == "__main__":
    main()
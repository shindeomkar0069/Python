def Factorial(No):
    fact = 1
        
    for i in range(1,No+1):
        fact = fact*i

    return fact

def main():
    value=int(input("Enter number"))

    Ret = Factorial(value)

    print(f"factotial of {value} is {Ret}")


if __name__=="__main__":
    main()
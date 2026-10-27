def Factorial(No):
    Fact = 1
        
    for i in range(1,No+1):
        fact = fact*i

    return fact

def main():
    value=int(input("Enter number"))

    Ret = Factorial(value)

    print("factotial is:",Ret)


if __name__=="__main__":
    main()
from Marvellous import Addition

def main():
    print("Enter first number:")
    Value1 = int(input())

    print("Enter the Second Number:")
    Value2 = int(input())

    Ret =Addition(Value1,Value2)
    Ret =Substraction(Value1,Value2)   #Error

    print("Addition is:",Ret)
    print("Substraction is :",Ret)
    
if __name__ == "__main__":
    main()  
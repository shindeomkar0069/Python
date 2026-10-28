def main():
    Ans=0
    try:
        print("Enter First Number:")
        No1=int(input())

        print("Enter Second Number:")
        No2=int(input())

        Ans=No1/No2
        print("Division is Sucessful")
    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is Zero:",zobj)

    except ValueError as vobj:
        print("Exception due to Invalide Data Type:",vobj)

    except Exception as eobj:
        print("Exception occured :",eobj)
    print("Result is:",Ans)

if __name__=="__main__":
    main()
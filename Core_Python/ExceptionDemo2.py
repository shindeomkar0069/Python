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
    print("Result is:",Ans)

if __name__=="__main__":
    main()
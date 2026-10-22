def Summetion(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no
    return Sum

def main():
    Size = 0
    Arr = list()

    print("Enter the NUmber of elements:")
    Size = int(input())

    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = Summetion(Arr)
    print("Summetion is:",Ret)

if __name__ == "__main__":
    main()  
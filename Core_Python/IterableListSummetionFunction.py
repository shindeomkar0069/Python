def Summetion(Data):
    Sum = 0

    for no in Data:
        Sum = Sum+no
    return Sum

def main():
    Marks =[78,90,56,98,77]
    Ret = Summetion(Marks)
   
    print("Addition is:",Ret)

if __name__ == "__main__":
    main()  
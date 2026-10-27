def filterX(Task,Elements):
    Result =[]
    for no in Elements:
        Ret = Task(no)   #CheckEven(no)
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task,Elements):
    Result=[]
    for no in Elements:
        Ret = Task(no)  #Increament(no)
        Result.append(Ret)
    return Result    

def reduceX(TasK,Elements):
    Sum = 0

    for no in Elements:
        Sum = TasK(Sum,no)
    return Sum

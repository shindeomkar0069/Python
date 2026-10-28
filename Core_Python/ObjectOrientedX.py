class Arithematic:
    #Ret=Addition(Aobj,Value1,Value2)
    def Addition(self,No1,No2):  
       Ans=No1+No2
       return Ans

    def Substraction(self,No1,No2):  
       Ans=No1-No2
       return Ans

Aobj=Arithematic()
print("Enter first Number")
Value1=int(input())

print("Enter Second Number")
Value2=int(input())

Ret = Aobj.Addition(Value1,Value2)
print("Addition is:",Ret)

Ret =Aobj.Substraction(Value1,Value2)
print("Substraction is:",Ret)
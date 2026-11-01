class Demo:
    #class Variables
    Value1=10
    Value2=20

    def __init__(self):
        self.No1=11
        self.No2=21

    #instance Method
    def fun(self):
        print("Inside Instance Method Named As fun")
        print(self.No1)
        print(self.No2)
        print(self.Value1)
        print(self.Value2)

dobj=Demo()
dobj.fun()
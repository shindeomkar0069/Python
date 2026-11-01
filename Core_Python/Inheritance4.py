class Base:
    
    def fun(self):
        print("inside base fun")
    

class Derived(Base):
    pass


dobj=Derived()
dobj.fun()
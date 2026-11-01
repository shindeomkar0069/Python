class Base:
    def fun(self):
        print("inside base fun")


class Derived(Base):
    def fun(self):
        print("inside derived fun")


dobj = Derived()
dobj.fun()
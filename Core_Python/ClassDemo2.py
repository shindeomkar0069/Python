class Demo:
    def __init__(self):
        print("Inside Constructor")

    def __del__(self):
        print("inside Distructor")

obj1=Demo()
obj2=Demo()

print("End of Application")
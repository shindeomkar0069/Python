no = 11   #Global Variable

def Display():
    a = 21
    print("From Display:",no)
    print("From Display Value od a is:",a) #Local Variable 
   
    
def Demo():
    print("From Demo Value of a is :",a)
    print("From Demo:",no)

Display()
Demo()


import time 

def Factorial(No):
    fact = 1
        
    for i in range(1,No+1):
        fact = fact*i

    return fact

def main():
    value=int(input("Enter number"))

    start_time=time.time()

    Ret = Factorial(value)

    end_time=time.time()

    print(f"factotial of {value} is {Ret}")

    print(f"Time Requried is: {end_time-start_time:.5f} Seconds")



if __name__=="__main__":
    main()

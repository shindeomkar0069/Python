import time
import os
import multiprocessing

#sequence PID MAIN,PID SUM PPID SUM,SEMMENTIN SUM,PID ODD.PPID ODD ,TiME 


def SumEven(No):
   print(f"PID of SumEven:{os.getpid()}    PPID of SumEven is:{os.getppid()}")
   Sum = 0

   for i in range(2,No,2):
       Sum = Sum+i
    
   print("Summetion of Even :",Sum)


def SumOdd(No):
    print(f"PID of SumOdd:{os.getpid()}     PPID of SumOdd is:{os.getppid()}")
    Sum = 0

    for i in range(1,No,2):
       Sum = Sum+i
    
    print("Summetion of Odd :",Sum)
    
    
def main():
    print(f"PID of main:{os.getpid()} PPID of main is:{os.getppid()}")
    start_time=time.perf_counter()
    
    t1 = multiprocessing.Process(target=SumOdd,args=(100000000,))
    t2 = multiprocessing.Process(target=SumEven,args=(100000000,))
     
    t1.start()
    t2.start()

    t1.join
    t2.join

    end_time=time.perf_counter()


    print(f"Time Requried is: {end_time-start_time:.4f} ")
    

if __name__ == "__main__":
    main()

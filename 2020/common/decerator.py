from datetime import datetime
from functools import wraps
import numpy as np

def dotwice(func):
    @wraps(func)
    def _dotwice(*args,**kwargs): 
        res1 = func(*args,**kwargs)
        res2 = func(*args,**kwargs)
        return res1,res2
    return _dotwice 

def main(): 
    prove1(5)

def time(func):

    def _time(*args,**kwargs):
        start = datetime.now()
        res = func(*args,**kwargs)
        end = datetime.now() 
        print(f" total time is {(end - start).total_seconds()} seconds")
        return res
    return _time
#@dotwice
#@time
def prove1(number): 
    """
    Prints number given as input,returns 2xnumber
    """
    doublezero = dotwice(np.zeros)
    number = doublezero([5])
    print(number)
    return number*2



print(prove1(5))
print(prove1.__doc__)
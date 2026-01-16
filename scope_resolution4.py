# varriable scope = where a varriable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Built In
from math import e

def func1():
    print(e)

e = 3

func1()

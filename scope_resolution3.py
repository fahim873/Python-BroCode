# varriable scope = where a varriable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Global

def func1():
#    x = 1
    print(x)

def func2():
#    x = 2
    print(x)

x = 3


func1()
func2()
print()
func1()
func2()

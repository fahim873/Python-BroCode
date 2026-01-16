# varriable scope = where a varriable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()
print()
func1()
func2()

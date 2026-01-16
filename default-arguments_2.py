import time
#def count(start=0, end):
def count(end, start=0):
    for x in range(start, end+1):
      print(x)
      time.sleep(1)
    print("Done!")

#count (5)
count(10,5)

from sys import argv

from time import localtime


def printarguments():
    for arg in argv:
        print(arg,"", end="")


start=localtime().tm_sec
print("start",start)
printarguments()
end=localtime().tm_sec
print("end",end)
timediff=end-start
print(f" end-start {end-start}")


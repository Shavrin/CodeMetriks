import os
import sys

arguments = sys.argv
def hello():
    global minimumSize
    class colors:
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

    #print("Number of arguments: " , len(arguments))
    #print("Arguments:" , arguments)

    if len(arguments) > 2:
        print(colors.FAIL , "Too many arguments." , colors.ENDC)
        exit(1)
    if len(arguments) == 2:
        minimumSize = int(arguments[1])



files = os.listdir()
extension = "exe"
minimumSize = 200 #bytes

hello()


for x in files:
    fileSize = os.path.getsize(x)
    if fileSize > minimumSize:

        fileExtension = x.split('.')
        fileExtension = fileExtension[len(fileExtension) - 1]

        if fileExtension == extension:
            os.remove(x)

    print(x , fileSize, "bytes")
    

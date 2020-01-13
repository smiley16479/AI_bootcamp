import sys

def usage():
    print ("Usage: python operations.py\nExample:\n    python operations.py 10 3")

def inputError():
    print ("InputError: too many arguments\n")

def inputError1():
    print("InputError: only numbers\n")

num1 = 0
num2 = 0
del sys.argv[0]
if len(sys.argv) < 2:
    usage()
    sys.exit(0)
elif len(sys.argv) > 2:
    inputError()
    usage()
    sys.exit(0)
else :
    try:
        num1 = int(sys.argv[0])
        num2 = int(sys.argv[1])
    except:
        inputError1()
        usage()
        sys.exit(0)
print("Sum:\t" + str(num1 + num2))
print("Difference:\t" + str(num1 - num2))
print("Product:\t" + str(num1 * num2))
try:
    print("Quotient:\t" + str(num1 / num2))
except:
    print("Quotient:\t ERROR (div by zero)")
try:
    print("Remainder:\t" + str(num1 % num2))
except:
    print("Remainder:\t ERROR (modulo by zero)")

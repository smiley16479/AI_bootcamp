import sys

del sys.argv[0]
sys.argv.reverse()
string = " ".join(sys.argv[::-1])
print (string[::-1].swapcase())

# File: myprog.py
import sys
print("User supplied", len(sys.argv)-1, "arguments.")
print("Arguments:", sys.argv)

# Print only the arguments
for i in range(1, len(sys.argv)):
    print("Argument ", i, " is: ", sys.argv[i])
    

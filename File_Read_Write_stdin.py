#!/usr/bin/python

import sys

file_name=sys.argv[1]
jackpot_number='23'
winning_number=0
try:
    # open file stream
    file = open(file_name, "w")
except IOError:
    print("There was an error writing to", file_name)
    sys.exit()
try:
    file = open(file_name, "a")
except IOError:
    print("There was an error reading file")
    sys.exit()
while winning_number != jackpot_number:
    winning_number = input("Enter number: ")
    if winning_number == jackpot_number:
        # close the file
        file.write("CONGRATULATIONS your winning number is "+ jackpot_number)
        file.write("\n")
        file.write("YOU HAVE WON A JACKPOT!!!")
        file.close()
        break
    else:
        print("Please,Try some different number")

file=open(file_name,"r")
fileRead = file.read()
print(fileRead)
file.close()

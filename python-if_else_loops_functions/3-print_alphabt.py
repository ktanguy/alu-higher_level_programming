#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    tanguy = chr(i)
    if tanguy not in "qe":
        print("{:s}".format(tanguy), end="")

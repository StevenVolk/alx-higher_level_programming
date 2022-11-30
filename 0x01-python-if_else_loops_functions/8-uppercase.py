#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if (97 <= ord(str[i]) and 122 >= ord(str[i])):
            upper += chr(ord(str[i]) - 32)
        else:
            upper += str[i]
    print("{}".format(upper))

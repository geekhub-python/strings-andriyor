#!/usr/bin/env python3

string = input()
if string.count('f') == 1:
    print(string.index('f'))
elif string.count('f') >= 2:
    print(string.index('f'), string.rindex('f'))

#!/usr/bin/env python3

string = input()
if string.count('f') == 1:
    print(-1)
elif string.count('f') >= 2:
    print(string.index('f', string.index('f') + 1))
else:
	print(-2)

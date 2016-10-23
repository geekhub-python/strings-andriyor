#!/usr/bin/env python3

s = input()
first = s.index('h') 
second = s.rindex('h') + 1
print(s[:first] + s[second:])

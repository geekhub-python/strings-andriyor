#!/usr/bin/env python3

s = input()
a = s.index('h') + 1
c = s.rindex('h')
b = (s[a:c].replace('h', 'H'))

print(s[:a] + b + s[c:])

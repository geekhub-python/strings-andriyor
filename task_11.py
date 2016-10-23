#!/usr/bin/env python3

s = input()
print((s[s.index('h') + 1:s.rindex('h')])[::-1])

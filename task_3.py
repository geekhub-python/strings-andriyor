#!/usr/bin/env python3

s = input() 
s1 = s[:int(round(len(s)/2))] 
s2 = s[len(s)//2:len(s)] 
s3 = s2 +s1 
print(s3)

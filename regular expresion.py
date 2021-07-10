import re

handle = open('regex_sum_595883.txt')

sum = 0
ls = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    ls = ls.append(stuff)
for digits in ls:
    sum = sum +int(digits)
print(sum)
    
    

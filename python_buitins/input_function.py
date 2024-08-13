# This challenge is only forPython 2.

# input()
# In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

# Code

# >>> input()  
# 1+2
# 3
# >>> company = 'HackerRank'
# >>> website = 'www.hackerrank.com'
# >>> input()
# 'The company name: '+company+' and website: '+website
# 'The company name: HackerRank and website: www.hackerrank.com'

# Task
# You are given a polynomial P of a single indeterminate (or variable), x.
# You are also given the values of x and k. Your task is to verify if P(x) = k.

# Constraints
# All coefficients of polynomial P are integers.
# x and y are also integers.

# Input Format
# The first line contains the space separated values of x and k.
# The second line contains the polynomial P.

# Output Format
# Print True if P(x) = k. Otherwise, print False.

# Sample Input
# 1 4
# x**3 + x**2 + x + 1

# Sample Output
# True

# Explanation
# P(1) = 1^3 + 1^2 + 1 + 1 = 4 = k

# Hence, the output is True.
# Precisa refatorar

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

X, K = map(int, input().split())
P = list(re.split(" ", input()))
polynomial_sum = 0
count = 0
num = 1


for value in P:
    value = value.strip()
    if value[0].isnumeric():
        num = int(value[0])
    if "**" in value and count > 0 and "+" in P[count-1]:
        polynomial_sum += num * X ** int(value[-1])
    elif "**" in value and count > 0 and "-" in P[count-1]:
        polynomial_sum -= num * X ** int(value[-1])
    elif "**" in value:
        polynomial_sum += X ** int(value[-1])
    elif value.isnumeric() and "-" in P[count-1]:
        polynomial_sum -= int(value[-1])
    elif value.isnumeric() and "+" in P[count-1]:
        polynomial_sum += int(value[-1])
    elif "+" in P[count-1]:
        polynomial_sum += X
    elif "-" in P[count-1]:
        polynomial_sum -= X
    count += 1
    
print(polynomial_sum == K)

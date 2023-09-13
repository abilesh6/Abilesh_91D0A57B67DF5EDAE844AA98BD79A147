# 1.1 implement a recursive function to calculate the factorial of a given number.
"""
1!=1x1
2!=2x1---->>2x1
3!=3x2---->>3x2x1
.
.
.
.
.
.
10!=10x9!--->>10x9x8x...x1

formula - n x (n-1)!
"""


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter a value:"))
res = fact_rec(number)

print("The Factorial of {} is {}.".format(number, res))

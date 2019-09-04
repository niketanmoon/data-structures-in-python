'''
Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function.
'''
n = int(input("Enter the integer"))
def sumOfSquares(n):
    return sum([i*i for i in range(1,n)])
print(sumOfSquares(n))
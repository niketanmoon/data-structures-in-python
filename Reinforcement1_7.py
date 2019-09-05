'''
Give A single command that computes the sum from Exercise R1.6 relying on Python's comprehension syntax and the built-in sum function
'''
n = int(input("Enter the integer "))
def sumOfSquares(n):
    return sum([i*i for i in range(1,n,2)])
print(sumOfSquares(n))
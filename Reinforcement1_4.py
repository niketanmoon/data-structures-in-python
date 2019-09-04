'''Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers
smaller than n'''
sum = 0
n = int(input("Enter the integer "))
for i in range(1,n):
    sum = sum + i**2
print(sum)

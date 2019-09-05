'''
Write a short python function that takes a positive integer n and returns the sum of the squares of all the positive odd integers smaller than n
'''
n = int(input("Enter the number "))
result = 0
for i in range(1,n,2):
    result = result + (i*i)
print(result)
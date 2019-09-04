'''
Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built in functions min or max in implementing your solution
'''
list_data = []
n = int(input("How many numbers you wanna put? "))
for i in range(n):
    m = int(input("Enter the number you want to put in the List"))
    list_data.append(m)

def minmax(data):
    sorted(data)
    result = (data[0],data[-1])
    print(result)

minmax(list_data)
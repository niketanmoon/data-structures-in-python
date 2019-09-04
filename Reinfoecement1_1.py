#Write a short Python function, is_multiple(n,m), that takes two integer values and returns True if n is a multiple of m, that is,
#n=mi for some integer i, and False otherwise

def is_multiple(n,m):
    for i in range(1,m+1):
        if m*i == n:
            return True

    return False

n = int(input("Enter the first number you want to find the multiple of: "))
m = int(input("Enter the number you wanna check"))

print(is_multiple(n,m))
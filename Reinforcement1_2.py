'''Write a short Python function, is_even(k), that takes an integer value and returns True if k is even and False otherwise. However your function
cannot use the multiplication, modulo or division operators'''

#We are going to use & logic operator
def is_even(k):
    if k & 1:
        return False
    else:
        return True
n = int(input("Enter the number you want to check for even numbers"))
print(is_even(n))
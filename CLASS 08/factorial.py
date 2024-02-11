def recursion(n):
    if n==0 or n == 1:
        return 1
    else:
        return n+recursion(n-1)
user_input=eval(input("Enter the number : "))
a=recursion(user_input)
print(a)
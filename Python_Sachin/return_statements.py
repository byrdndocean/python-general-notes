# The return statement is used to return or exit from the function and go back to the place where it was called from.

# Write a function to check if number is even or odd,
# if even print even
# if odd print odd

def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


output = even_or_odd(30)
output2 = even_or_odd(31)
print(output)
print(output2)

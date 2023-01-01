# input = "udemy"

# output = ['u', 'd', 'e', 'm', 'y']

# output = []
# input = 'udemy'
# for i in input:
#     output.append(i)
# print(output)
# ['u', 'd', 'e', 'm', 'y']


# /////////////////////////////////////////////////

# Using List Comprehension

# input = 'udemy'
# output = [i for i in input]
# print(output)
# we get ['u', 'd', 'e', 'm', 'y']

# ////////////////////////////////////////////////////

# List Comprehension
# [expression loop]

# input = [1, 2, 3, 4, 5]
# output = [i + 100 for i in input]
# print(output)
# we get [101, 102, 103, 104, 105]

# ///////////////////////////////////////////////////

# List Comprehension
# [expression loop conditional]

# [expr   for   if]

# WAP to print all even numbers from 0 to 20 in a list
output = [i for i in range(0, 21) if i % 2 == 0]
print(output)
# we get [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# print each 1 out
for i in range(0, 21):
    if i % 2 == 0:
        print(i)

# While loop

# write a loop to print numbers starting from 0 to 5

# count = 0
# while count <= 5:
#     print(count)
#     count = count + 1


# ////////////////////////////////////////

# WARNING INFINITE WHILE LOOP
# while True:
#     print(count)
#     count = count + 1

# ///////////////////////////////////////////////

# FINITE GAME LOOP
# useful if you want to take some input from the user
# if you want to take some input from the keyboard or mouse
count = 0
while True:
    print(count)
    count = count + 1

    if count > 5:
        break

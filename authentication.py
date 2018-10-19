from userAuth import *



def is_valid(username,password):
    validUsers = getUsers("users.txt")
    for key in validUsers:
        if key == username and validUsers[key] == password:
            return (True)

    return (False)


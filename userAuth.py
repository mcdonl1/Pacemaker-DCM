#User authentication

def testing():
    fileName = "users.txt";
    d1 = {"u1":"p1", "u2":"p2", "u3":"p3", "u4":"p4"}
    d2 = {"a":"b","c":"d"}
    updateFile(fileName, d1)
    
    print(getUserN(fileName))
    print(getUsers(fileName))
    print(addUser(fileName, "addU1", "addP1"))
    print(addUser(fileName, "addU1", "addP1"))
    print(addUser(fileName, "addU2", "addP1"))
    print(getUserN(fileName))
    print(getUsers(fileName))
    print(delUser(fileName, "u2"))
    print(getUserN(fileName))
    print(getUsers(fileName))
    print(clearUsers(fileName))
    print(getUserN(fileName))
    print(getUsers(fileName))
    print(isEmpty(fileName))

def isEmpty(fName):
    'returns True if there are 0 users, False otherwise'
    f = open(fName, "r")
    if (f.read() == "0\n"):
        f.close()
        return True
    f.close()
    return False

def getUsers(fName):
    'returns a dictionary of all users where key is the username'
    if (isEmpty(fName)):
        return {}

    userDict = {}
    f = open(fName, "r")
    n = int(f.readline())
    for i in range(n):
        pair = f.readline().strip("\n").split(",")
        userDict[pair[0]] = pair[1]
    f.close()
    return userDict

        
def getUserN(fName):
    'returns the number of logged in users ie the first line'
    if (isEmpty(fName)):
        return {}
    
    f = open(fName, "r")
    ans = f.readline().strip("\n")
    f.close()
    return ans


def addUser(fName, user, passw, confirmpassw):
    'adds the user into file f. Returns 1 if successful, 0 if user already exists'
    data = getUsers(fName)
    if user not in data:
        if passw == confirmpassw:
            data[user] = passw
        else:
            return 0
        updateFile(fName, data)
        return 1
    return 0


def delUser(fName, user):
    'deletes the user from file. Returns 1 if success, 0 if user not in file'
    if (isEmpty(fName)):
        return 0
    
    data = getUsers(fName)
    if user in data:
        del data[user]
        updateFile(fName, data)
        return 1
    return 0


def updateFile(fName, data):
    'writes the file fName with data (assuming data is dictionary)'
    f = open(fName, "w")
    f.write(str(len(data)) + "\n")

    k = list(data.keys())
    v = list(data.values())

    for i in range(len(data)):
        f.write(k[i] + "," + v[i] + "\n")

    f.close()


def clearUsers(fName):
    'removes all users'  
    updateFile(fName, {})
    


#testing()
    

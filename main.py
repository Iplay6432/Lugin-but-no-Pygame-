import regex as re
def mainscree():
    print("What Would YOu Like To Do Today?")
    print("1: Setup")
    print("2: Login")
    print("3: Reset Password")
    choice = input("")
    if choice == "1":
        Setup()
    elif choice == "2":
        Login()
    elif choice == "3":
        resetpass()
    else:
        print("Invalid Choice")
        mainscree()
def Setup():
    info = open("example.uiwaygusduowauh", "a")
    print("")
    print("")
    print("")
    print("What Would You Like Your Username to Be?")
    setemail = input("")
    print("What Would You Like your password to be?")
    setpass = input("")

    print("Where Was you First School (Recovery)")
    setrecov = input("")
    setemail = str(setemail)
    setpass = str(setpass)
    setrecov = str(setrecov)
    if setemail == setpass or setemail == setrecov or setrecov== setpass:
        print("Password, Email, and Recovery Cannot Be The Same")
        Setup()
    info.write(f"[{setemail} {setrecov}" + "] \n")
    info.write(f"[{setemail} 1 {setpass}]")

def Login():
    info = open("example.uiwaygusduowauh", "r")
    print("")
    print("")
    print("")
    print("What Is Your Username?")
    user = input()
    print("What Is Your Password?")
    pwass = input()
    allinfo = f"[{user} 1 {pwass}]"
    print(allinfo)
    if allinfo in info:
        print('String', allinfo, 'Found In File')
    else:
        print("Incorrect Password/Username")

def resetpass():
    info = open("example.uiwaygusduowauh", "r")
    print("What Is Your Email?")
    email = input("")
    print("What is Your Recovery Info? (Where Was Your First School?)")
    recov = input()
    allinfo = f"[{email} {recov}]"
    print(allinfo)
    if allinfo in info:
        print('String', allinfo, 'Found In File')
        print("What Would You Like Your New Password to Be?")
        newpass = input()
        with open("example.uiwaygusduowauh", 'r+') as f:
            text = f.read()
            text = re.sub(f"[{email}1", f"[{email} {newpass}]", text)
            f.seek(0)
            f.write(text)
            f.truncate()
    else:
        print("Incorrect Password/Username")
def loggedin():
    print("it workced")
mainscree()

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
    damp = email + " 1"
    flag = 0
    index = 0
    for line in info:  
        index += 1 
        if allinfo in line:
        
            flag = 1
            break 
    if flag == 0: 
        print('String', allinfo , 'Not Found') 
    else:
        print('String', allinfo, 'Found In File')
        print("What Would You Like Your New Password to Be?")
        newpass = input()
        file = open("example.uiwaygusduowauh")
        lines = file.readlines()
        file.close
        for i in range(len(lines)):
            #flag = 0
            #index = 0
            """
            for line in info:  
                index += 1 
                if damp in lines:        
                    flag = 1
                    break 
            if flag == 0: 
                print(damp)
                print('String', damp , 'Not Found') 
                """
            #else:
            if True:
                print(damp)
                print(lines[i])          
                if damp in lines[i]:
                    #balance = (lines[i])
                    balance = ("[" + email + " 1 " + newpass +"]")
                    lines[i] = (balance)
                    print("worked???")
                else:
                    print("didnt work")
        file = open("example.uiwaygusduowauh", "w")
        file.write("")
        file.writelines(lines)
        file.close
def loggedin():
    print("it workced")
mainscree()

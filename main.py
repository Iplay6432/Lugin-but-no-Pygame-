import regex as re
try:
    tt = open("example.uiwaygusduowauh")
    tt.close
except:
    d = open("example.uiwaygusduowauh", "x")
    d.close
def split(word):
    return [char for char in word]
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
    info.write(f"[{setemail} {setrecov}] \n")
    info.write(f"[{setemail} 1 {setpass}] \n")
    info.close
    mainscree()

def Login():
    info = open("example.uiwaygusduowauh", "r")
    print("")
    print("")
    print("")
    print("What Is Your Username?")
    user = input()
    print("What Is Your Password?")
    pwass = input()
    allinfo = "["+ user + " 1 " + pwass + "]"
    print(allinfo)
    flag = 0
    index = 0
    for line in info:  
        index += 1 
        if allinfo in line:
            flag = 1
            break 
    if flag == 0:
        print("Incorrect Password/Username")
    else: 
        print('String', allinfo, 'Found In File')
        print("What Would You Like to Do?")
        print("1: Check Your Balance/Walet")
        print("2: Deposit Money")
        print("3: Get Money")
        choice = input("")
        if choice == "1":
            ccb(user)
        if choice == "2":
            checkwal(user)
        if choice == "3":
            getmon(user)

def getmon(user):
        x=1
def checkwal(user):
    info = open("example.uiwaygusduowauh", "r")
    talfe = "["+ user + " BAntLEancEESS "
    flag = 0
    index = 0
    for line in info:  
        index += 1 
        if talfe in line:
            flag = 0
            break 
    if flag == 1: 
        info.close
        print("L")
        tinfo = open("example.uiwaygusduowauh", "a")
        tianfy= "["+ user + " BAntLEancEESS " + "10" "]"
        tinfo.write(tianfy + "\n")
        print("workced??")
        tinfo.close
    else:
        print('String', tianfy, 'Found In File')
def depmon(user):
    info = open("example.uiwaygusduowauh", "r")
    tnalfe = "["+ user + " BAntLEancEESS "
    
    file = open("example.uiwaygusduowauh")
    lines = file.readlines()
    file.close
    
    for i in range(len(lines)):
        if True:        
            if tnalfe in lines[i]:
                tnalfe = lines[i]
def writemon(user, tnalfe):
    print(tnalfe)
    lits = tnalfe
    lits=tnalfe
    lits=str(lits)
    lits = lits.split(' ')
    del lits[0]
    del lits[0]
    stringg = ''.join(str(x) for x in lits)
    print(stringg)
    x = stringg.replace("]", "", 1)
    y = stringg.replace("]", "", 1)
    y = int(y)
    print("Your Walet has $" +x)
    print ("How much money do you want put into your bank Account?")
    monadd=input("")
    montadd = int(monadd)
    if montadd > y():
        print("Incorrect Number, Try again, It is greater than your walet")
    elif montadd <= y():
        lb()
        writeyybal(user, x,tnalfe)
def writeyybal(user,addbal,tnalfe):
    balfe = "["+ user + " &5!5 "
    file = open("example.uiwaygusduowauh") 
    lines = file.readlines()
    file.close
    for i in range(len(lines)):
        if True:
            print(balfe)
            print(lines[i])          
            if balfe in lines[i]:
                balance = (balfe )
                lines[i] = (balance)
                print("worked???")
            else:
                print("didnt work")
        file = open("example.uiwaygusduowauh", "w")
        file.write("")
        file.writelines(lines)
        file.close
def ccb(username):
    info = open("example.uiwaygusduowauh", "r")
    balfe = "["+ username + " &5!5 "
    flag = 0
    index = 0
    for line in info:  
        index += 1 
        if balfe in line:
            flag = 1
            break 
    if flag == 0: 
        info.close
        print("L")
        tinfo = open("example.uiwaygusduowauh", "a")
        balty = "["+ username + " &5!5 " + "5" "]"
        tinfo.write(balty + "\n")
        print("workced??")
        tinfo.close
        lb(balfe,username) 
    else:
        print('String', balfe, 'Found In File')
        lb(balfe,username)     
def lb(balfe,user):    
    file = open("example.uiwaygusduowauh")
    lines = file.readlines()
    file.close
    for i in range(len(lines)):
        if True:        
            if balfe in lines[i]:
                balfe = lines[i]
                showbal(user, lines[i])
                

def showbal(user,balfe):
    print(balfe)
    lits = balfe
    lits=balfe
    lits=str(lits)
    lits = lits.split(' ')
    del lits[0]
    del lits[0]
    stringg = ''.join(str(x) for x in lits)
    print(stringg)
    x = stringg.replace("]", "", 1)
    print("Your Balance is " + "$" +x)
    return x
def resetpass():
    info = open("example.uiwaygusduowauh", "r")
    print("What Is Your Email?")
    email = input("")
    print("What is Your Recovery Info? (Where Was Your First School?)")
    recov = input()
    allinfo ="[" + email + " " + recov + "]"
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
            if True:
                print(damp)
                print(lines[i])          
                if damp in lines[i]:
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

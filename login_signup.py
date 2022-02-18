import json
print("Welcome to my Login-Signup")
print("1.signup, 2.login")
n=input("Enter any number")
if n=="1":
    username=input("Enter any username=")
    password=input("Enter any password=")
    if (password>="a" and password<="z") or (password>="A" and password<="Z") or (password>=0 and password<=9) or (password=="@", "!","&","_"):
        if len(password)>=6 and len(password)>=12:
            print("Your password is Correct.")
        else:
            print("Sorry, Your password is incorrect.")
    description=input("Enter your description:")
    DOB=input("Enter your DOB:")
    hobbies=input("Enter your hobbies:")
    gender=input("Enter your gender:")
    a=[username]
    b=[password]
    c=[description]
    d=[DOB]
    e=[hobbies]
    f=[gender]
    i=0
    dic1={}
    dic2={}
    dic3={}
    dic4={}
    dic5={}
    dic6={}
    dic7={}
    dic8={}
    dic9={}
    dic10={}
    dic11={}
    dic12={}
    dic13={}
    while i<len(a):
        dic1=username
        dic2=password
        dic3=description
        dic4=DOB
        dic5=hobbies
        dic6=gender
        i=i+1
    dic7["username"]=dic1
    dic8["password"]=dic2
    dic9["description"]=dic3
    dic10["DOB"]=dic4
    dic11["hobbies"]=dic5
    dic12["gender"]=dic6
    dic13.update(dic7)
    dic13.update(dic8)
    dic13.update(dic9)
    dic13.update(dic10)
    dic13.update(dic11)
    dic13.update(dic12)
    a=json.dumps(dic13)
    print(a)
    with open("Barsha.json","w") as file:
        json.dump(dic13,file,indent=4)
if n=="2":
    username=input("Enter any username=")
    password=input("Enter any password=")
    if (password>="a" and password<="z") or (password>="A" and password<="Z") or (password>=0 and password<=9) or (password=="@", "!","&","_"):
        if len(password)>=6 and len(password)>=12:
            print("Your password is Correct.")
        else:
            print("Sorry, Your password is incorrect.")
    list1=[username]
    list2=[password]
    i=0
    dic1={}
    dic2={}
    dic3={}
    dic4={}
    dic5={}
    while i<len(list1):
        dic1=username
        dic2=password
        i=i+1
    dic3["username"]=dic1
    dic4["password"]=dic2
    dic5.update(dic3)
    dic5.update(dic4)
    a=json.dumps(dic5)
    print(a)
    if username in "Barsha.json":
        print("Username is already exist")
    elif username not in "Barsha.json":
        print("Username is allow")
    with open("Barsha.json","w") as file:
        json.dump(dic5,file,indent=4)


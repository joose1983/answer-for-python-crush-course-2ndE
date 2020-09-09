#usernames=['jackie','admin','tom','jenny','rebecca']
usernames=[]
if usernames==[]:
    print("we need to find some users!")
else:
    for name in usernames:
        if name=='admin':
            print("hello admin, do you want to check the report?")
        else:
            print("thank you for logging in again")
        

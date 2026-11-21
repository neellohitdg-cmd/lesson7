student=input("Do u have any medical issues?[y/n]").lower()
if student=="y":
    print("Np you r allowed :D")
else:
    attendance=int(input("What was your attendance percentage?:"))
    if attendance>=75:
        print("u r allowed :D")
    else:
        print("u r not allowed :(")
#meow meow meow
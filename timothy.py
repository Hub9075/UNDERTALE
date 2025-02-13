import time
def timothy():
    print("Warninig youv'e encountered timothy you have 3 options")
    time.sleep(2)
    print("1.hug him,  2. dance with him, 3.tell him your secrets")
    time.sleep(3)
    choice = input("choice: ")
    if choice == "1":
        print("Youve hugged timothy for some reason he likes it")
    elif choice == "2":
        print("You dance with timothy hes feeling the vibe")
    elif choice == "3":
        print("You tell timothy your secret hes disgusted")
        return spare()
    
def spare():
    print("Timothy angered you now you have a choice")
    time.sleep(4)
    print("1. kill him 2.spare")
    choice = input("choice: ")
    if choice == "1":
        print("You are in jail for 99999999 hours")
    elif choice == "2":
        print("You live to old age congrats i guess")




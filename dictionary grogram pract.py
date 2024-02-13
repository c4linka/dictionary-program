"""Program for user to:
    1. Add definition
    2. Serch for definition
    3. Erase definition
"""
defDict = {}


while(True):
    print("MENU.")
    print("Hello, check the menu below:")
    print("1. - is for adding the definition pairs")
    print("2. - is for finding the definition pairs")
    print("3. - is for deleting the definition pairs")
    print("4. - is for closing the definition program")

    action = input("Choose action number: ")

    if action == "1":
        elements=int(input("Write number of definitions would you like to add. "))
        if elements > 0: 
            for i in range(elements):
                key =  input(str("Write a word to define: "))
                value = input(str("Write word's definition: "))
                print("Definition/s has been added")
                defDict[key] = value
            print("Adding done.")
            print("\n")

        else:
            print("\n")
            print("Choose number bigger then 0. Start from the beggining")
            print("\n")

    elif action == "2":
        serchKey = input("Write a word to find it's definition: ")
        if serchKey in defDict:
            print(defDict[serchKey])
            print()

        else:
            print("No such word in dictionary")
            print()

    elif action == "3":
        delKey = input("Which word with it's definition would you like to erese? ")
        if delKey in defDict:
            del(defDict[delKey])
            print(delKey,"has been deleted from dictionary.")
            print()

        else:
            print("No such word in dictionary")
            print()

    elif action == "4":
        print("OK! That's all folks! Have a nice day, goodbye! ;)")
        break

    else:
        print("\n")
        print("ERROR! Choose the right number from MENU below.")
        print("\n")
        

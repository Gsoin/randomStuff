accept=str(input("Would you like to interact with this menu?"))
accept.lower();

while accept == "yes":
    
    print("Select one of the options:")
    print("1. Lookup animal babies") 
    print("2. Add animal and baby")
    print("3. Delete animal and baby")
    print("4. Exit")

    selection=str(input("Please Select(1,2,3,4):"))

    if selection =='1':
        animal = {"hippo" : "calf",
               "horse" : "foal",
               "dog" : "pup",
               "kangaroo" : "joey",
               "monkey" : "infant",
               "owl" : "owlet",
               "parrot" : "chick",
               "rabbit" : "bunny",
               "rat" : "pup",
               "cow" : "calf",
               "skunk" : "kit",
               "sheep" : "lamb"}
        
        question = input("Which animal would you like to know about: ")
        question = question.lower();

        print("The baby of a "+question + " is called a "+ animal.get(question,"I don't know that yet!"))
        accept=str(input("Would you like to interact with this menu again?"))
        accept.lower();

    elif selection == '2':
        animal = {"hippo" : "calf",
               "horse" : "foal",
               "dog" : "pup",
               "kangaroo" : "joey",
               "monkey" : "infant",
               "owl" : "owlet",
               "parrot" : "chick",
               "rabbit" : "bunny",
               "rat" : "pup",
               "cow" : "calf",
               "skunk" : "kit",
               "sheep" : "lamb",}
        
        key = input("Enter the animal name: ")
        val = input("Enter the baby name: ")
        animal[key]=(val)
        print("Your entry has been added!")
        print("Thanks for using me!")
        accept=str(input("Would you like to interact with this menu again?"))
        accept.lower();
    elif selection == '3':
        animal = {"hippo" : "calf",
               "horse" : "foal",
               "dog" : "pup",
               "kangaroo" : "joey",
               "monkey" : "infant",
               "owl" : "owlet",
               "parrot" : "chick",
               "rabbit" : "bunny",    
               "rat" : "pup",
               "cow" : "calf",
               "skunk" : "kit",
               "sheep" : "lamb",}
        
        name = str(input("Enter the animal name: "))
        del animal[name]
        print("Your entry has been deleted!")
        print("Thanks for using me!")
        accept=str(input("Would you like to interact with this menu again?"))
        accept.lower();
        
    elif selection == '4': 
        exit()
        
    else: 
          print ("Unknown Option Selected!")



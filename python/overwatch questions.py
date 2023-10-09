
character1 = str(input("Is it a guy or girl"  ))
if character1 == "girl":
    character2=input("is she a brunette")
    if character2 == "yes":
        print("Is the character Tracer")
    if character2=="no":
        print("Is the character Junker Queen")
if character1=="no":
    character3 = input ("is the man black ")
    if character3=="yes" :
        print ("Is the character the Master of knockbacks The Doomfist")
    if character3=="no":
        character5= input("Is he American")
        if character5== "yes":
            print ("Is your character Lifeweaver")
        if character5=="no":
            character7=input("Is he blonde")
            if character7=="yes":
                print("Is your character Soldier 76")
            if character7=="no":
                print("Is your character Death AKA Reaper")
else :
    print ("Invalid answer use yes or no")

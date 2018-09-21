# Færa punkt í hnitakerfi þar sem hvert hnit er X,Y hnit.
# Upphafspunktur 1,1 og enda punktur 3,1.
# Tilfærslur eru skilgreindar (N)orður, (S)uður, (A)ustur og (V)estur.
# Hreyfing fyrir hverja tilfærslu getur verið:
    # N => Y + 1
    # S => Y - 1
    # E => X + 1
    # W => X - 1
# Fastar stærðir verði: Max = 3 og Min = 1 fyrir bæði X og Y. Notaðir eru
# sömu Fastar fyrir X og Y þar sem í þessu tilviki þær eru 1 og 3 fyrir 
# báða ásana (axis).
# Upphafspunktur er 1,1 þar sem eingöngu er hægt að fara (N)orður. Næsti reitur
# er þá 1,2 þar sem mögulegar hreyfingar eru (N)orður, (S)uður eða (A)ustur.
# Svo koll af kolli.
# Hindranir í hnitakerfinu eru:
    # 1,1 er bara hægt að fara (N)orður
    # 2,1 er bara hægt að fara (N)orður
    # 2,2 er bara hægt að fara (V)estur
    # 2,3 er bara hægt að fara (A)ustur og (V)estur
    # 3,2 er bara hægt að fara (N)orður og (S)uður

# Github repo:
# https://github.com/gunnsteinng07/Tile_Traveler

#Breytur fyrir hreyfingu leikmannsins í völundarhúsinu
x = 1
y = 1
#Strengur fyrir innslátt áttar sem ferðast á í
str_movement = ""


#while lykkja sem keyrir þangað til að x = 3 og y = 1
while x != 3 or y != 1:
    if x == 1 and y == 1: #1,1
        print("You can travel: (N)orth.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n":
            print("Not a valid direction!")
            str_movement = input("Direction: ")
            str_movement = str_movement.lower()
        y += 1
    elif x == 1 and y == 2: #1,2
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n" or str_movement != "e" or str_movement != "s":
            if str_movement == "n":
                y += 1
                break
            elif str_movement == "e":
                x += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 1 and y == 3: #1,3
        print("You can travel: (E)ast or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "e" or str_movement != "s":
            if str_movement == "e":
                x += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 2 and y == 1: #2,1
        print("You can travel: (N)orth.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n":
            print("Not a valid direction!")
            str_movement = input("Direction: ")
            str_movement = str_movement.lower()
        y += 1
    elif x == 2 and y == 2: #2,2
        print("You can travel: (S)outh or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "s" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 2 and y == 3: #2,3
        print("You can travel: (E)ast or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "e" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "e":
                x += 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 3 and y == 3: #3,3
        print("You can travel: (S)outh or (W)est.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "s" or str_movement != "w":
            if str_movement == "w":
                x -= 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()
    elif x == 3 and y == 2: #3,2
        print("You can travel: (N)orth or (S)outh.")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
        while str_movement != "n" or str_movement != "s":
            if str_movement == "n":
                y += 1
                break
            elif str_movement == "s":
                y -= 1
                break
            else:
                print("Not a valid direction!")
                str_movement = input("Direction: ")
                str_movement = str_movement.lower()

#Lykkjan búin og þar með sigrinum náð, prenta það.
print("Victory!")
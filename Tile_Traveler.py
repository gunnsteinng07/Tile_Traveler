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


Max = 3
Min = 1
x = 1
y = 1
final_tile = False

if x == Max and y == Min:
    final_tile = False
else:
    final_tile = True

# While loopan sem ætti að nota
while final_tile:

    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "n":
            x += 0
            y += 1
        else:
            print("Not a valid direction!")
        print(x,",",y)

    elif x == 1 and y == 2:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "n":
            x += 0
            y += 1
        elif movement == "e":
            x += 1
            y += 0
        elif movement == "s":
            x += 0
            y -= 1
        else:
            print("Not a valid direction!")
        print(x,",",y)
        
    elif x == 1 and y == 3:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "e":
            x += 1
            y += 0
        elif movement == "s":
            x += 0
            y -= 1
        else:
            print("Not a valid direction!")
        print(x,",",y)

    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "n":
            x += 0
            y += 1
        else:
            print("Not a valid direction!")
        print(x,",",y) 

    elif x == 2 and y == 2:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "w":
            x -= 1
            y += 0
        elif movement == "s":
            x += 0
            y -= 1
        else:
            print("Not a valid direction!")
        print(x,",",y)

    elif x == 2 and y == 3:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "w":
            x -= 1
            y += 0
        elif movement == "e":
            x += 1
            y += 0
        else:
            print("Not a valid direction!")
        print(x,",",y)

    elif x == 3 and y == 3:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "w":
            x -= 1
            y += 0
        elif movement == "s":
            x += 0
            y -= 1
        else:
            print("Not a valid direction!")
        print(x,",",y)
    
    elif x == 3 and y == 2:
        print("You can travel: (N)orth.")
        movement = input("Direction: ")
        movement = movement.lower()
        if movement == "n":
            x += 0
            y += 1
        elif movement == "s":
            x += 0
            y -= 1
        else:
            print("Not a valid direction!")
        print(x,",",y)


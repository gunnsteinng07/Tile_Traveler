# Verkefnið er það sama og Tile_Traveler1.py. Hér hefur verið bætt við föllum til að
# einfalda kóðann sem og til að koma í veg fyrir endurtekningar í kóðanum.
# Grunnhugmyndin að kóðanum er sú sama og í fyrri úrlausninni en reynt er að stytta kóðann
# með föllum.

# Answers:
# 1. In the second implementation I could work on the problem in smaller peaces, divide-and-conquer
  # method. Then I could build the final code up using those smaller peaces.
# 2. In my opinion the second code is easier to read because repeated actions have been put into one
  # definition and then the actual code itself calls the function.
# 3. It was possible to reduce the amount of repeat code by a large amount 
  # since the functions can be called when needed rather than having those lines of code for each separate instance.

# Github repo:
# https://github.com/gunnsteinng07/Tile_Traveler

# Breytur fyrir hreyfingu leikmannsins í völundarhúsinu
x = 1
y = 1

def valid_directions(x,y):
    # Tekur við stöðu notanda í völundarhúsinu og skilar streng með þeim áttum
    if (x == 1 and y == 1) or (x == 2 and y == 1): #1,1
        # print("You can travel: (N)orth.")
        return "n"
    elif x == 1 and y == 2: #1,2
        # print("You can travel: (N)orth or (E)ast or (S)outh.")
        return "nes"
    elif x == 1 and y == 3: #1,3
        # print("You can travel: (E)ast or (S)outh.")
        return "es"
    elif (x == 2 and y == 2) or (x == 3 and y == 3): #2,2
        # print("You can travel: (S)outh or (W)est.")
        return "sw"
    elif x == 2 and y == 3: #2,3
        # print("You can travel: (E)ast or (W)est.")
        return "ew"
    elif x == 3 and y == 2: #3,2
        # print("You can travel: (N)orth or (S)outh.")
        return "ns"

def print_directions(directions):
    # Fall sem tekur inn streng, fer í gegnum hann og bætir áttum við strenginn og prentar út
    all_directions = "You can travel: "
    temp_string = directions
    for chars in temp_string:
        if "n" in temp_string:
            all_directions += "(N)orth"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("n", "")
        elif "e" in temp_string:
            all_directions += "(E)ast"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("e", "")    
        elif "s" in temp_string:
            all_directions += "(S)outh"
            if len(temp_string) > 1:
                all_directions += " or "
            temp_string = temp_string.replace("s", "")
        elif "w" in temp_string:
            all_directions += "(W)est"
    all_directions += "."
    print(all_directions)
    return directions

def direction(valid_directions):
    # Kannar hvaða átt notandinn slær inn og athugar hvort að það er átt sem er í lagi og skilar svo áttinni sem notandinn færir sig í
    str_movement = input("Direction: ")
    str_movement = str_movement.lower()
    while str_movement not in valid_directions:
        print("Not a valid direction!")
        str_movement = input("Direction: ")
        str_movement = str_movement.lower()
    return str_movement

def mov_arithmetic(x, y, str_direction):
    # Tekur við núverandi stöðu x,y í hnitakerfinu og áttin sem notandi vill hreyfa sig í. Skilar tuple sem mig minnir að maður þurfi
    # að afpakka með því að kalla í fallið með "x, y = mov_arithmetic(x,y,str_direction)"
    if str_direction == "n":
        y += 1
    elif str_direction == "s":
        y -= 1
    elif str_direction == "e":
        x += 1
    elif str_direction == "w":
        x -= 1
    return x,y

# Strengir til að senda í föllin
str_wherecanto = ""
str_checkdirection = ""

while x != 3 or y != 1:
    str_wherecanto = valid_directions(x,y)
    str_whereconto = print_directions(str_wherecanto)
    str_checkdirection = direction(str_wherecanto)
    x, y = mov_arithmetic(x, y, str_checkdirection)
# x, y = mov_arithmetic(x, y, print_directions(direction(valid_directions(x,y))))

print("Victory!")
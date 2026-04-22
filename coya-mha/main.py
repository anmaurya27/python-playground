#Project: MHA (Choose Your Own Adventure) / (Choice-based interactive fiction)


print(r'''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((
''')

print("Welcome to the Tutorial (level 0)")
print("Your goal is to find the Lost Artifact")

location1 = "0"
location2 = "0"

cross_road = input("You are at a cross road. What will you choose? "
                   "'left' or 'right' or 'forward' =  ").lower()

if cross_road == "left":
    print("Game Over, you can't go left")

elif cross_road == "forward":
    lake = input("You are at a lake. What will you choose? "
                 "'wait' or 'swim' = ").lower()
    if lake == "wait":
        location1 = "wait"
        print("You have arrived at a house")
    else:
        print("Game Over, you can't swim")

elif cross_road == "right":
    castle = input("You are at a castle. What will you choose? "
                   "'gate' or 'wall' = ").lower()
    if castle == "wall":
        hall = input("You are at a hall. What will you choose? "
                     "'house' or 'hut' = ").lower()
        if hall == "house":
            location2 = "house"
        else:
            print("Game Over, there was a monster in the hut")
    else:
        print("Game Over, you can't go through gate")

if location1 == "wait" or location2 == "house":
        chest = input("You found four chests. What will you choose? "
                      "'chest1' or 'chest2' or 'chest3' or 'chest4' = ")
        if chest == "chest3":
            print("You found the Lost Artifact")
        elif chest == "chest1":
            print("Game Over")
        elif chest == "chest2":
            print("Game Over")
        elif chest == "chest4":
            print("Game Over")



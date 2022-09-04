#link: http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def jump():
    while wall_in_front():
        turn_left()
        move()
        turn_right()
    if not wall_in_front():
        move()
        turn_right()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()  

while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        jump()
"""SceneSwitch I"""
def switch():
    """This is show program to think of SceneSwitch I"""
    state = "off"
    count = 0
    pretime = 0
    while True:
        time = input()
        if time == "End":
            break
        time = float(time)
        if state == "off":
            state = "cool"
        elif state == "cool":
            state = "offcool"
        elif state == "offcool":
            difftime = time - pretime
            if difftime <= 6:
                state = "warm"
                count += 1
            else:
                state = "cool"
        elif state == "warm":
            state = "off warm"
        elif state == "off warm":
            state = "cool"
        pretime = time
    print(count)
switch()

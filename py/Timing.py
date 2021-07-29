#NUTPAPAT YOUYOUNG 60070024
"""Timing II"""
def calculate_time(time):
    """This is Show Program Calculate Timeing"""
    days = time // (60*60*24)
    time = time % (60*60*24)
    hours = time // (60*60)
    time = time % (60*60)
    minutes = time // 60
    sec = time % 60
    if days < 0:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d" %(days, hours, minutes, sec))
calculate_time(int(input()))

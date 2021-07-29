"""Timing II"""
def calculate_time(seconds):
    """This is Show Program Calculate Timeing"""
    if seconds < 0:
        print("ERR_:__:__:__")
    elif seconds > 863999999:
        print("ERR_:__:__:__")
    else:
        days = seconds // (60*60*24)
        seconds %= (60*60*24)
        hours = seconds // (60*60)
        seconds %= (60*60)
        minutes = seconds // 60
        seconds %= 60
        print("%04d:%02d:%02d:%02d" %(days, hours, minutes, seconds))
calculate_time(int(input()))

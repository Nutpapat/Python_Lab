"""ParkingCar Problem"""
def parking(inpark, outpark):
    """Return Price of Parking time from given time(inpark and out park)"""
    inpark = int(inpark[:2])*60 + int(inpark[3:])
    outpark = int(outpark[:2])*60 + int(outpark[3:])
    if outpark > inpark:
        diff = outpark - inpark-15
        if diff % 60 != 0:
            diff = diff//60 +1
        else:
            diff = diff//60
    else:
        diff = 1440 - (inpark-outpark) - 15
        if diff % 60 != 0:
            diff = (diff//60) +1
        else:
            diff = diff//60
    print(diff*15)
 
parking(input(), input())
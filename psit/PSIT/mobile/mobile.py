"""MobileCallPromotion Problem"""
def promotion(time, sum_price):
    """Return price of Promotion from given timecall(second)"""
    time = second_to_minute(time)
    for (pro, price) in [(24*60, 150), (12*60, 100), (8*60, 80), (3*60, 40), (60, 15), (20, 10)]:
        sum_price = sum_price + (time//pro)*price
        time = time % pro
    oneminute = time - 3
    return sum_price + oneminute if oneminute > 0 else sum_price

def second_to_minute(time):
    """Convert second to minute"""
    if time % 60 != 0:
        time = time + 60
    return time // 60

print(promotion(int(input()), 0))

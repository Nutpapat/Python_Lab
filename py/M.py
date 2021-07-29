"""Additive"""
import math
def function():
    """Calculate Function"""
    func_1 = math.sin(math.radians(90)) + (math.sin(math.radians(60))**2)
    func_2 = math.cos(math.radians(245**2)) + math.cos(math.radians(45+135))
    func_3 = func_1/func_2
    func_4 = (math.factorial(16)*math.factorial(4))/math.factorial(8)
    func_5 = 15 + 25
    func_6 = math.sqrt(((25-12)**2) + ((12-15)**2))
    func_7 = func_5/func_6
    func_8 = math.log((1234**4), 10)
    func_9 = math.log(4234, 5) + math.log(8191, 2) + 71*math.log(156154, 10)
    func_10 = math.log(777, 7) - math.log(888, 8) - math.log(999, 9)
    func_11 = func_9/func_10
    print(func_3)
    print(func_4)
    print(func_7)
    print(func_8)
    print(func_11)
function()

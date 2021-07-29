"""CircularPrime Problem"""
def is_prime(number):
    """Return True if number is prime, false otherwise"""
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            return False
    return True
 
def circle_str(number):
    """switch char in string"""
    number = str(number)
    for num in range(1, len(number)):
        word_num = number[num:]+number[:num]
        if is_prime(int(word_num)):
            pass
        else:
            return False
    return True
 
def coprime(num, sum_prime):
    """find from 1 to n and Print sum prime from given number(int)"""
    for number in range(1, num+1):
        if is_prime(number) and number != 1:
            if circle_str(number):
                sum_prime += number
    print(sum_prime)
 
coprime(int(input()), 0)
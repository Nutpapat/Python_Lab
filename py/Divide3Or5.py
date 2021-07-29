"""Divide3Or5"""
def main():
    """This is Show Program Find the sum of integers."""
    number = int(input())
    count = 0
    for i in range(1, number+1):
        if i%3 == 0 or i%5 == 0:
            count += i
    print(count)
main()

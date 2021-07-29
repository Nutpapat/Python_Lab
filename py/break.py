""" Week 11 - 60070024 && 60070031 """
import hashlib as hl
import codecs as cd
def main():
    """ BreakPassword """
    password = input()
    for i in range(0, 99999):
        i = "%05d" % i
        if (hl.sha512(cd.encode(i)).hexdigest().upper()) == password:
            print(i)
            break
main()

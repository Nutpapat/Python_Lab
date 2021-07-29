""" Week 11 - 60070024 && 60070031 """
import hashlib as hl
import codecs as cd
def main():
    """ WordSequence II """
    password = input()
    print(hl.sha512(cd.encode(password)).hexdigest().upper())
main()

"""Sequence XXX"""
def main():
    """This is show program Sequence XXX"""
    nnn = int(input())
    mmm = int(input())
    side = 0
    center = nnn-4
    print(("*" * nnn + " ") * mmm)
    for _ in range((nnn-3)//2):
        print(("*" + " "*side + "*" + " "*center + "*" + " "*side + "* ") * mmm)
        side += 1
        center -= 2
    if nnn > 1:
        print(("*" + " "*side + "*" + " "*side + "* ") * mmm)
    for _ in range((nnn-3)//2):
        side -= 1
        center += 2
        print(("*" + " "*side + "*" + " "*center + "*" + " "*side + "* ") * mmm)
    if nnn > 1:
        print(("*" * nnn + " ") * mmm)
main()

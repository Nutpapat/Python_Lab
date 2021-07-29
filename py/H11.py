"""Seven"""
def main():
    """Seven"""
    name = input()
    rice = int(input())
    sandwhich = int(input())
    sarapow = int(input())
    water = int(input())
    snack = int(input())
    #name
    print("Employee :", name)
    #money
    arc_rice = ""
    arc_sandwhich = ""
    arc_sarapow = ""
    arc_water = ""
    arc_snack = ""
    price = 0
    if rice >= 25:
        price += 30*2*rice
        arc_rice = "R "
    else:
        price += rice*30
    if sandwhich >= 40:
        price += 25*2*sandwhich
        arc_sandwhich = "S "
    else:
        price += sandwhich*25
    if sarapow >= 70:
        price += 20*2*sarapow
        arc_sarapow = "P "
    else:
        price += sarapow*20
    if water >= 100:
        price += 15*2*water
        arc_water = "W "
    else:
        price += water*15
    if snack >= 250:
        price += 10*2*snack
        arc_snack = "K "
    else:
        price += snack*10
    print("Payday :", (price), "Bath.")
    print("Archivement :", arc_rice + arc_sandwhich + arc_sarapow + arc_water + arc_snack)
    #chom
    print("You did great!,", name+".")
main()

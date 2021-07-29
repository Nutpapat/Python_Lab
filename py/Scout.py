"""Scout"""
def main():
    """Boil an egg for tiger"""
    var_egg_amog_wight = int(input())
    for _ in range(var_egg_amog_wight):
        n_max, weight_max = [int(x) for x in input().split()][1:]
        eggs = sorted([int(x) for x in input().split()])
        weight = 0
        ans_egg = 0
        for i in eggs:
            if weight+i <= weight_max and ans_egg+1 <= n_max:
                weight += i
                ans_egg += 1
        print(ans_egg)
main()

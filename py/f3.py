"""Pick"""
def main():
    """This is show program Pick"""
    import json
    dic = json.loads(input())
    key = input()
    if key in dic:
        print("Yes")
        print(dic[key])
    else:
        print("No")
main()

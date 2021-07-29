"""stats"""
def stats(number):
    """Print stats"""
    list1 = []
    for _ in range(number):
        list1.append(float(input()))
    mean = sum(list1)/number
    if mean%1 == 0:
        print("Mean =", int(mean))
    else:
        print("Mean = "+("%.4f" % mean))
    findmode(list1)
    findmed(list1)
    findsd(list1)

def findmode(list1, i=0):
    """Print Mode"""
    for j in range(len(list1)):
        if list1.count(list1[j]) > i:
            mode = list1[j]
            i = list1.count(list1[j])
    if mode%1 == 0:
        print("Mode =", int(mode))
    else:
        print("Mode = "+("%.4f" % mode))

def findmed(list1):
    """Print Med"""
    list1.sort()
    if len(list1) % 2 != 0:
        med = ((len(list1))+1)//2
        med = (list1[med-1])
    else:
        med = (list1[int((len(list1))/2)]+list1[int((len(list1)/2)-1)])/2
    if med%1 == 0:
        print("Med =", int(med))
    else:
        print("Med = "+("%.4f" % med))

def findsd(list1, sum_sd=0):
    """Print SD"""
    mean = sum(list1)/len(list1)
    for j in range(len(list1)):
        sum_sd += (list1[j]-mean)**2
    sum_sd = ((1/((len(list1))-1))*sum_sd)**0.5
    if sum_sd%1 == 0:
        print("SD =", int(sum_sd))
    else:
        print("SD = "+("%.4f" % sum_sd))
stats(int(input()))

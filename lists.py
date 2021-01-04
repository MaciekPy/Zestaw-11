import random


def initlist(n):
    nums = []
    for i in range(n):
        nums.append(i)
    return nums


def randlist(n):
    randnums = initlist(n)
    random.shuffle(randnums)
    return randnums


def easylist(n):
    easy = initlist(n)
    for i in range(1, n):
        j = random.randint(i - 1, i)
        easy[i], easy[j] = easy[j], easy[i]
    return easy


def reverselist(n):
    revlist = easylist(n)
    revlist.reverse()
    return revlist


def gausslist(n):
    gauss = []
    for _ in range(n):
        gauss.append(random.gauss(0, 1))
    return gauss


def ksetlist(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(0, n // 2))
    return nums

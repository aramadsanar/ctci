str_1 = 'caebne'
str_2 = 'abeced'

def check_permutation(x, y):
    if (len(x) != len(y)):
        return False

    xsort = sorted(x)
    ysort = sorted(y)

    for i in range(len(xsort)):
        if xsort[i] != ysort[i]:
            return False
    return True

print(check_permutation(str_1, str_2))
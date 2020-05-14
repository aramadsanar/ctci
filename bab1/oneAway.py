str_1_eqlen = 'pale'
str_2_eqlen = 'bake'


str_1 = 'pale'
str_2 = 'ple'


def one_away(str_1, str_2):
    if (len(str_1) == len(str_2)):
        return one_away_eqlen(str_1, str_2)
    else:
        return one_away_neqlen(str_1, str_2)

def one_away_eqlen(str_1, str_2):
    found_diff = False
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            if found_diff:
                return False
            found_diff = True
    return True

def one_away_neqlen(str_1, str_2):
    i = 0
    j = 0
    diff = 0

    shorter_str = str_1 if len(str_1) < len(str_2) else str_2
    longer_str = str_1 if len(str_1) > len(str_2) else str_2

    while i < len(shorter_str) and j < len(longer_str):
        if str_1[i] != str_2[j]:
            diff += 1
            if str_1[i + 1] == str_2[j]:
                i += 1
            if str_2[j + 1] == str_1[i]:
                j += 1
        i += 1
        j += 1

    return diff < 2

print(one_away(str_1_eqlen, str_2_eqlen))
print(one_away(str_1, str_2))

print(one_away('pale', 'bale'))
print(one_away('pales', 'pale'))
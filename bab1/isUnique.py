str_1 = 'abcd'
str_2 = 'abece'

def is_unique(input):
    chars = {}
    for c in input:
        if (chars.get(c)):
            return False
        chars[c] = True
    return True

print(is_unique(str_1))
print(is_unique(str_2))
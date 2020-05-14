str_in = 'tact coa'

def check_odd_count(counter):
    found_odd = False
    for c in counter:
        if found_odd:
            return False
        if counter.get(c) % 2 == 1:
            found_odd = True

    return True

def palindrome_permutation(str_in):
    counter = {}
    
    for c in str_in:
        if c == ' ':
            continue
        if not counter.get(c):
            counter[c] = 1
        else:
            counter[c] += 1
    print(counter)
    return check_odd_count(counter)
    
print(palindrome_permutation(str_in))
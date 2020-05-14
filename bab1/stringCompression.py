input_str = 'aabcccccaaa'

def compress_str(input_str):
    result = ''
    i = 0

    while i < len(input_str):
        current_char = input_str[i]
        # print(current_char)
        count_current_char = 0

        # print(result)
        while input_str[i] == current_char:
            count_current_char += 1
            i += 1

            if i > len(input_str) - 1:
                break
            if input_str[i] != current_char:
                break
        
        
        result += str(current_char) + str(count_current_char)

    return result if len(result) < len(input_str) else input_str

print(compress_str(input_str))
print(compress_str('abcd'))
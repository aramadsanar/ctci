input = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]

def nullify(input, i, j):
    for x in range(len(input)):
        input[x][j] = 0
    for y in range(len(input[0])):
        input[i][y] = 0

def nullify_array(input):
    arr_res_flag = [[False for i in range(len(input[0]))] for j in range(len(input))]

    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 0:
                arr_res_flag[i][j] = True

    for i in range(len(arr_res_flag)):
        for j in range(len(arr_res_flag[0])):
            if arr_res_flag[i][j]:
                nullify(input, i, j)

    
    print(arr_res_flag)

    return input

print(nullify_array(input))
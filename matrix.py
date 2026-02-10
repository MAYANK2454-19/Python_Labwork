mat1 = [[1,1,1],
        [2,2,2],
        [3,3,3]]

mat2 = [[1,1,1],
        [2,2,2],
        [3,3,3]]

# initialize result matrix with zeros
mat3 = [[0,0,0],
        [0,0,0],
        [0,0,0]]

# check if multiplication is possible
if len(mat1[0]) == len(mat2):
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k] * mat2[k][j]
            mat3[i][j] = sum

# print result
for row in mat3:
    print(row)

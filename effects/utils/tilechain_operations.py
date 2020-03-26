
# prints the Matrix to the console in Pretty
def prettyMatrixPrint(matrix):

    buff = ""

    for i in matrix:
        for j in i:
            buff += str(j) + " "
        buff += "\n"
    print(buff)

# gets one 8x8 block from a (2^n * 2^n) Matrix
def getTileFromBoard(matrix, indX, indY):
    startIndexX = indX * 8
    endIndexX = (indX + 1) * 8

    startIndexY = indY * 8
    endIndexY = (indY + 1) * 8

    tile = []
    temp = []

    for i in range(startIndexX, endIndexX):
        for j in range(startIndexY, endIndexY):
            temp.append(matrix[i][j])
        tile.append(temp)
        temp = []

    return tile

# places a tuple (where (x-cordinate,y-cordinate, value)) inside a matrix
def placeTupleInMatrix(arr, index, val):
    tempArr = []
    counter = 0

    for i in arr:
        if index == counter:
            tempArr.append(val)
        else:
            tempArr.append(i)
        counter += 1

    return tempArr

# places a list of tuples (where (x-cordinate,y-cordinate, value)) inside of a matrix
def placeListInMatrix(matrix, toPlace):
    temp = toPlace.copy()

    for i in temp:
        matrix[i[1]] = placeTupleInMatrix(matrix[i[1]], i[0], i[2])

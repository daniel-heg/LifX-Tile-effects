
def prettyMatrixPrint(matrix):

    buff = ""

    for i in matrix:
        for j in i:
            buff += str(j) + " "
        buff += "\n"
    print(buff)


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

def insertTupleIntoMatrix(arr, index, val):
    tempArr = []
    counter = 0

    for i in arr:
        if index == counter:
            tempArr.append(val)
        else:
            tempArr.append(i)
        counter += 1

    return tempArr


def placeListInMatrix(matrix, toPlace):
    temp = toPlace.copy()

    for i in temp:
        matrix[i[1]] = insertTupleIntoMatrix(matrix[i[1]], i[0], i[2])


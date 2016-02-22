import sys

#create a N X N matrix from the file
def constructMatrixFromFile(n,fname):
    lines = [line.rstrip('\n') for line in open(fname)]
    matrix = []
    for i in range(n):
        inside = []
        items=lines[i].split(',')
        for j in range(n):
            inside.append(items[j])
        matrix.append(inside)
    return matrix

#print the matrix
def printMatrix(m):
    for row in m:
        print row
    print

#rotate the matrix by 90 degrees (clockwise)
def rotate90Degrees(m):
    layers = len(m) / 2
    length = len(m) - 1

    for layer in range(layers): #for each layer
        for i in range(layer, length - layer): # loop through the elements we need to change at each layer
            temp = m[layer][i] #save the top element,
            #Left -> Top
            m[layer][i] = m[length - i][layer]
            #Bottom -> left
            m[length - i][layer] = m[length - layer][length - i]
            #Right -> bottom
            m[length - layer][length - i] = m[i][length - layer]
            #Top -> Right
            m[i][length - layer] = temp

#main function
def main():
    matrix = constructMatrixFromFile(8,'array.txt')
    print "Original matrix:\n"
    printMatrix(matrix)
    rotate90Degrees(matrix)
    print "Rotate matrix by 90 degrees:\n"
    printMatrix(matrix)
    rotate90Degrees(matrix)
    print "Rotate matrix by 90 degrees:\n"
    printMatrix(matrix)
    rotate90Degrees(matrix)
    print "Rotate matrix by 90 degrees:\n"
    printMatrix(matrix)

if __name__ == '__main__':
    main()

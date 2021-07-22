def printDoorMat(row, col):
    pattern = ".|."
    hyphen = "-"
    word = "WELCOME"

    for i in range(row):
        if i < (row - 1) / 2:
            print((pattern * (2 * i + 1)).center(col, "-"))
        elif i == (row - 1) / 2:
            print(word.center(col, "-"))
        else:
            print((pattern * (2*(row - 1 - i) + 1)).center(col, "-"))

if __name__ == '__main__':
    row, col = map(int, input().split(" "))
    printDoorMat(row, col)
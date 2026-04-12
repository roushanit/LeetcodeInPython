def getRow(rowIndex):
    row = [1]

    for i in range(1, rowIndex + 1):
        row.append(1)
        for j in range(i - 1, 0, -1):
            row[j] = row[j] + row[j - 1]

    return row

print(getRow(3))    

#########code using Using Binomial Coefficient formuala to get output
def getRow(n):
    row = [1]

    for k in range(1, n + 1):
        next_val = row[-1] * (n - k + 1) // k
        row.append(next_val)

    return row

print(getRow(3))

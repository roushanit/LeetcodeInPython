def generate(numRows):
    if numRows == 0:
        return []

    res = [[1]]

    for i in range(1, numRows):
        prev = res[-1]
        row = [1]

        for j in range(1, len(prev)):
            row.append(prev[j-1] + prev[j])

        row.append(1)
        res.append(row)

    return res
    
print(generate(5))    

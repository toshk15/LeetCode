def allCellsDistOrder(rows,cols,rCenter,cCenter):
    res= []

    for r in range(rows):
        for c in range(cols):
            res.append([r,c])
    res.sort(key=lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))
    return res

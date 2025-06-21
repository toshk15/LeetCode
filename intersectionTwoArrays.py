def intersectionTwoArrays(arr1, arr2):
    inter = set(arr1)
    res = [] 
    for n in arr2:
        if n in inter:
            res.append(n)
            inter.remove(n)
    return res

arr1 = [1,2,2,3,4]
arr2 = [0,2,4,5,6]

print(intersectionTwoArrays(arr1, arr2))
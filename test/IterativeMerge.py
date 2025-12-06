"""

def merge(l, r):
    if not len(l) or not len(r):
        return l or r
    
    result = []
    i, j = 0, 0
    while len(result) < (len(l) + len(r)):
        if l[i] < r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
    return result

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    l = mergeSort(arr[:mid])
    r = mergeSort(arr[mid:])

    return merge(l, r)



    def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)
    
        return merge(l,r)

def merge(l, r):

    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
        
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1
    return arr


arr = [12,11,13,7,9,1]
print(mergeSort(arr))
"""


def Imerge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        Imerge(l)
        Imerge(r)
        return merge(l,r)
    
    

def merge(l,r):
    i=j=k=0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j+=1
        k += 1
    
    while i < len(l):
        arr[k] = l[i]
        k += 1
        i += 1

    while j < len(r):
        arr[k] = r[j]
        k += 1
        j += 1
    return arr

    

arr = [12,11,13,7,9,1]
print(Imerge(arr))

    
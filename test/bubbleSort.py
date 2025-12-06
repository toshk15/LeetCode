def bubbleSort(arr):

    flag = True
    n = len(arr)

    for i in range(n):
        flag = False
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        
        if flag == False:
            break
    return arr

arr = [1,2,3,4,5,6]
print(bubbleSort(arr))
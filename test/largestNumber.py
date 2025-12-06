from functools import cmp_to_key
def largesNumber(arr):
    for i, n in enumerate(arr):
        arr[i] = str(n)

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
        
    arr = sorted(arr, key=cmp_to_key(compare))
    return str(int("".join(arr)))

arr = [1,35,2,4] 
print(largesNumber(arr))

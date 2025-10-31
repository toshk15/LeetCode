def canPlaceFlowers(flowerbed, n):
    flowerbed = [0]+flowerbed+[0]
    for i in range(1,len(flowerbed)):        
        if i+1<len(flowerbed) and flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            flowerbed[i]=1
            n-=1
    return True if n<=0 else False
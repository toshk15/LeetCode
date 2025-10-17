def numRescueBoats(people,limit):
    people.sort()
    l=0
    c=0
    r=len(people)-1
    while l<=r:
        if people[l]+people[r]<=limit:
            l+=1
        c+=1
        r-=1
    return c

people = [3,2,2,1]
print(numRescueBoats(people, 3))
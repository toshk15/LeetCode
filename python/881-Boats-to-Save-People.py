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

"""
Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)

Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

"""
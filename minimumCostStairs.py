def minCostClimbingStairs(cost):
    n = len(cost)
    minCost=[0]*(n+1)
    for i in range(2,n+1):
        minCost[i] = min(cost[i-1]+minCost[i-1], cost[i-2]+minCost[i-2])
    return minCost[n]

cost=[4,8,15,16,23,42]
print(minCostClimbingStairs(cost))
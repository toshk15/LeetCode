def finalValueAfterOperations(self, operations):
    X=0
    for n in operations:
        if n=="--X" or n=="X--":
            X-=1
            
        if n=="++X" or n=="X++":
            X+=1
    return X

operations = ["--X","X++","X++"]
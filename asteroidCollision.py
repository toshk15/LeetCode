def asteroidCollision(asteroids):
    stack = []
    
    for a in asteroids:
        if a > 0:
            stack.append(a)
        else:
            while stack and stack[-1] > 0 and stack[-1] < -a:
                stack.pop()
            if stack and stack[-1] == -a:
                stack.pop()
            elif not stack or stack[-1] < 0:
                stack.append(a)
    return stack


#asteroids = [-1, 3, 2,-3]
asteroids = [1, 3, 5, -10]
print(asteroidCollision(asteroids))
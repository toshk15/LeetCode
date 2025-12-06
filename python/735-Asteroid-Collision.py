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


"""
class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        s = []

        for ast in a:
            while s and ast < 0 and s[-1] > 0:
                if ast + s[-1] == 0: #both destroyed
                    s.pop()
                    break
                elif ast + s[-1] < 0:
                    s.pop()
                else:
                    break
            else:
                s.append(ast)
        
        return s
"""


#asteroids = [-1, 3, 2,-3]
asteroids = [1, 3, 5, -10]
print(asteroidCollision(asteroids))

"""
Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:

Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
"""
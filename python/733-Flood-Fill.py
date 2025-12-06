class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        curr = image[sr][sc]
        q = deque()
        q.append((sr,sc))
        sett = set()
        sett.add((sr,sc))
        while q:
            r,c = q.popleft()
            image[r][c]=color

            directions=[[-1,0],[1,0],[0,1],[0,-1]]
            for dir in directions:
                nr = r + dir[0]
                nc = c + dir[1]

                if nr in range(row) and nc in range(col) and image[nr][nc]==curr and (nr,nc) not in sett:
                    q.append((nr,nc))
                    sett.add((nr,nc))
        return image
    
"""
Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

Explanation:

From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

"""
from collections import deque

def hasPath(maze, start, destination):   

        rows, cols = len(maze), len(maze[0]) 
        queue = deque([start])
        visited = set()
        visited.add(tuple(start))

        while queue:

            current_position = queue.popleft()
            row, col = current_position        

            for direction_row, direction_col in [[0, -1], [0, 1], [-1, 0], [1, 0]]:                            

                while 0 <= row + direction_row < rows and 0 <= col + direction_col < cols and maze[row + direction_row][col + direction_col] == 0:
                    row += direction_row
                    col += direction_col
                    #print(row, col)

                if [row, col] == destination:
                    return True

                if (row, col) not in visited:
                    visited.add((row, col))
                    queue.append((row, col))  
  
        return False
    
if __name__ == "__main__":
    maze = [
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0]]
start =  [0, 0]
end = [2, 2]

print(hasPath(maze, start, end))
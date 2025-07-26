def totalNQueens(n):  

        def dfs(row):
            if row == n:
                nonlocal solution_count
                solution_count += 1
                return

            for col in range(n):

                pos_diag = row + col
                neg_diag = row - col + n  

                if cols[col] or diag[pos_diag] or anti_diag[neg_diag]:
                    continue
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = True
                dfs(row + 1)
                cols[col] = diag[pos_diag] = anti_diag[neg_diag] = False


        cols = [False] * n  # Columns where the queens can attack
        diag = [False] * (2 * n)  # Positive diagonals (index = row + col)
        anti_diag = [False] * (2 * n)  # Negative diagonals (index = row - col + n)
        solution_count = 0  # Counter for number of valid solutions      

        dfs(0)
        return solution_count

print(totalNQueens(4))
#Solving n-queen problem using backtracking

def find_all_n_queens_solutions(n):
    
    def solve_n_queens_recursive(row, cols, diagonal1, diagonal2):
        if row == n:
            return [[]]

        solutions = []
        for col in range(n):
            if col not in cols and row + col not in diagonal1 and row - col not in diagonal2:
                cols.add(col)
                diagonal1.add(row + col)
                diagonal2.add(row - col)
                for sub_solution in solve_n_queens_recursive(row + 1, cols, diagonal1, diagonal2):
                    solutions.append([(row, col)] + sub_solution)
                cols.remove(col)
                diagonal1.remove(row + col)
                diagonal2.remove(row - col)
        return solutions

    cols = set()
    diagonal1 = set()
    diagonal2 = set()
    solutions = solve_n_queens_recursive(0, cols, diagonal1, diagonal2)
    return solutions
  
  def print_result(result):
    for i, solution in enumerate(result):
        print(f"Solution {i + 1}:")
        for row, col in solution:
            print(f"({row}, {col})", end=" ")
        print("\n")


n = int(input("Enter the number of queens: "))
result = find_all_n_queens_solutions(n)
print_result(result)

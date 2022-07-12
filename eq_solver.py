from fractions import Fraction

class Equation:

    def __init__(self, A, X):
        self.A = list(map(self.make_fraction_row, A))
        self.X = self.make_fraction_row(X)
        self.length = len(X)
    
    def make_fraction_row(self, row):
        return list(map(Fraction, row))

    def div_row_by(self, row_idx, x):
        for i in range(self.length):
            self.A[row_idx][i] /= x
        self.X[row_idx] /= x
    
    def mult_row(self, row_idx, x):
        new_row_A = []
        for i in range(self.length):
            new_row_A.append(self.A[row_idx][i] * x)
        new_const = self.X[row_idx] * x
        return (new_row_A, new_const)
    
    def sub(self, sub_elements, row_idx):
        sub_row, sub_X = sub_elements
        for i in range(self.length):
            self.A[row_idx][i] -= sub_row[i]
        self.X[row_idx] -= sub_X
            
    
    def solve(self):
        for i in range(self.length):
            self.div_row_by(i, self.A[i][i])
            for j in range(self.length):
                if i != j:
                    self.sub(self.mult_row(i, self.A[j][i]), j)
        
        return tuple(map(float, self.X))



def solve(A, X) -> "solution":
    """A is a 2d array which represents a matrix of coefficients (Left hand side)
    X is an array of constants (Right hand side).
    Returns an array which is a solution to the system of equation.
    
    Example:
    Consider you have a system of equation
    x + 2y + 3z = 14
    2x - 3y + 4q = 8
    4x - 2y + 3z = 9

    Then A = [
        [1, 2, 3],
        [2, -3, 4],
        [4, -2, 3]
    ]
    and X = [14, 8, 9]

    The function will return [1, 2, 3],
    which means that (x, y, z) = (1, 2, 3)
    is a solution.
    """
    return Equation(A, X).solve()
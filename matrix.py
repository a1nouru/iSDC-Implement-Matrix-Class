import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

### Need to define dot_product to ease the calculation of Matrix Multiplication
def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        print("error! Vectors must have same length")
    
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i] * vector_two[i]
    return result
###
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            determinanteValue = a*d - b*c
            return determinanteValue
        
        if self.h == 1:
            determinanteValue = self.g[0][0]
            return determinanteValue
        
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        sumDiagonal = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    sumDiagonal = sumDiagonal + self.g[i][j] 
                    
        return sumDiagonal
    
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            inverseMatrix = zeroes(1,1)
            inverseMatrix[0][0] = 1/self.g[0][0]
            return inverseMatrix
        
        if self.h == 2:
            inverseMatrix = zeroes(2, 2)
            determinantValue = self.determinant()
            inverseMatrix[0][0] = self.g[1][1] * (1/determinantValue)
            inverseMatrix[0][1] = -self.g[0][1] * (1/determinantValue)
            inverseMatrix[1][0] = -self.g[1][0] * (1/determinantValue)
            inverseMatrix[1][1] = self.g[0][0] * (1/determinantValue)
            return inverseMatrix
        
            
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrixTranspose = zeroes(self.w,self.h)
        for j in range(self.w):
            for i in range(self.h):
                matrixTranspose[j][i] = self.g[i][j]
        return matrixTranspose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        sumResult = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                sumResult[i][j] = self.g[i][j]+other.g[i][j]
        return sumResult
        
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        negResult = zeroes(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                negResult[i][j] = (-1 * self.g[i][j])
        return negResult

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        subResult = zeroes(self.h,self.w)
        negOther = - other 
        subResult = self + negOther
        return subResult

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        #Check if matrices don't have the same internal indicies, so that they couldn't be multiplied
        if self.w != other.h :
            raise(ValueError, "Matrices cannot be multiplied") 
        multResult = zeroes(self.h,other.w)
        otherTranspose = other.T()
        for i in range (self.h):
            for j in range (otherTranspose.h):
                multResult[i][j] = dot_product(self.g[i],otherTranspose.g[j]) #to avoid 3 nested loops, dot product function is defined
        return multResult
        
        
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            mulResult = zeroes(self.h,self.w)
            for i in range(self.h):
                for j in range(self.w):
                    mulResult[i][j] = (other*self.g[i][j])
            return mulResult
            
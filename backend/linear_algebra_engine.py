import numpy as np

class MatrixOps:
    """Class for basic matrix operations."""
    
    @staticmethod
    def add(A, B):
        return np.add(A, B)

    @staticmethod
    def subtract(A, B):
        return np.subtract(A, B)

    @staticmethod
    def multiply(A, B):
        return np.dot(A, B)

    @staticmethod
    def transpose(A):
        return np.transpose(A)

    @staticmethod
    def trace(A):
        return np.trace(A)

    @staticmethod
    def power(A, n):
        return np.linalg.matrix_power(A, n)

class LinearAlgebraSolver:
    """Class for advanced linear algebra tasks."""

    @staticmethod
    def determinant(A):
        return np.linalg.det(A)

    @staticmethod
    def inverse(A):
        try:
            return np.linalg.inv(A)
        except np.linalg.LinAlgError:
            return "Matrix is singular and cannot be inverted."

    @staticmethod
    def rank(A):
        return np.linalg.matrix_rank(A)

    @staticmethod
    def solve_linear_system(A, B):
        """Solves Ax = B."""
        try:
            return np.linalg.solve(A, B)
        except np.linalg.LinAlgError as e:
            return str(e)

    @staticmethod
    def eigenvalues(A):
        vals, vecs = np.linalg.eig(A)
        return vals, vecs

    @staticmethod
    def lu_decomposition(A):
        # We can use scipy if available, or just numpy for basic QR/SVD
        # For simplicity, let's stick to numpy for now or assume scipy is available
        from scipy.linalg import lu
        p, l, u = lu(A)
        return p, l, u

    @staticmethod
    def qr_decomposition(A):
        q, r = np.linalg.qr(A)
        return q, r

if __name__ == "__main__":
    # Test cases
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("Matrix A:\n", A)
    print("Matrix B:\n", B)
    print("A + B:\n", MatrixOps.add(A, B))
    print("A * B:\n", MatrixOps.multiply(A, B))
    print("Det(A):", LinearAlgebraSolver.determinant(A))
    print("Inverse(A):\n", LinearAlgebraSolver.inverse(A))
    
    vals, vecs = LinearAlgebraSolver.eigenvalues(A)
    print("Eigenvalues:", vals)

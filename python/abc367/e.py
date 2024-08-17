import numpy as np

def matrix_exponentiation(P, K, n):
    result = np.eye(n, dtype=int)  # Identity matrix of size n
    base = P.copy()
    
    while K > 0:
        if K % 2 == 1:
            result = np.dot(result, base) % n
        base = np.dot(base, base) % n
        K //= 2
    
    return result

def apply_permutation(A, P):
    return A[np.argmax(P, axis=0)]

# Input
n, k = map(int, input().split())
x = list(map(int, input().split()))
a = list(map(int, input().split()))

# Convert x to zero-based index
x = np.array(x) - 1

# Create permutation matrix P
P = np.zeros((n, n), dtype=int)
for i in range(n):
    P[x[i], i] = 1

# Compute P^K
P_k = matrix_exponentiation(P, k, n)

# Apply P^K to A
result = apply_permutation(np.array(a), P_k)

# Output the result
print(" ".join(map(str, result)))

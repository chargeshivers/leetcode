def binary_search(A, x):
    def bs(i, j):
        if i > j:
            return False
        if i == j:
            return A[i] == x
        mid = (i + j) // 2
        return bs(i, mid) if x <= A[mid] else bs(mid + 1, j)

    return bs(0, len(A) - 1)

#!/usr/bin/env python3
"""Sparse table — O(1) range minimum/maximum queries after O(n log n) build."""
import sys, math, random

class SparseTable:
    def __init__(self, arr, op=min):
        n = len(arr); k = int(math.log2(n)) + 1 if n else 0
        self.op = op; self.k = k; self.log = [0] * (n + 1)
        for i in range(2, n + 1): self.log[i] = self.log[i // 2] + 1
        self.table = [arr[:]]
        for j in range(1, k):
            row = []
            for i in range(n - (1 << j) + 1):
                row.append(op(self.table[j-1][i], self.table[j-1][i + (1 << (j-1))]))
            self.table.append(row)
    def query(self, l, r):
        j = self.log[r - l + 1]
        return self.op(self.table[j][l], self.table[j][r - (1 << j) + 1])

if __name__ == "__main__":
    random.seed(42)
    arr = [random.randint(1, 100) for _ in range(20)]
    st = SparseTable(arr, min)
    print(f"Array: {arr}")
    queries = [(0,4),(3,7),(10,19),(0,19),(5,5)]
    for l, r in queries:
        print(f"  min[{l}:{r}] = {st.query(l, r)} (brute: {min(arr[l:r+1])})")

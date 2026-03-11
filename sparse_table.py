#!/usr/bin/env python3
"""Sparse table — O(1) range minimum/maximum queries after O(n log n) preprocessing.

One file. Zero deps. Does one thing well.
"""
import math, sys

class SparseTable:
    def __init__(self, arr, op=min):
        n = len(arr)
        self.op = op
        self.k = max(1, int(math.log2(n)) + 1) if n > 0 else 1
        self.table = [list(arr)]
        for j in range(1, self.k):
            prev = self.table[j - 1]
            half = 1 << (j - 1)
            row = []
            for i in range(n - (1 << j) + 1):
                row.append(op(prev[i], prev[i + half]))
            self.table.append(row)
        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

    def query(self, l, r):
        """Query [l, r] inclusive."""
        j = self.log[r - l + 1]
        return self.op(self.table[j][l], self.table[j][r - (1 << j) + 1])

def main():
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    st = SparseTable(arr, min)
    print(f"Array: {arr}")
    queries = [(0, 3), (2, 7), (0, 10), (5, 5)]
    for l, r in queries:
        print(f"  min[{l}..{r}] = {st.query(l, r)}")
    st_max = SparseTable(arr, max)
    for l, r in queries:
        print(f"  max[{l}..{r}] = {st_max.query(l, r)}")

if __name__ == "__main__":
    main()

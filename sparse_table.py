#!/usr/bin/env python3
"""Sparse Table for range minimum/maximum queries — zero-dep."""
import math

class SparseTable:
    def __init__(self, arr, fn=min):
        self.n=len(arr); self.fn=fn
        self.k=int(math.log2(self.n))+1 if self.n else 0
        self.table=[[0]*self.n for _ in range(self.k)]
        self.table[0]=list(arr)
        for j in range(1,self.k):
            for i in range(self.n-(1<<j)+1):
                self.table[j][i]=fn(self.table[j-1][i],self.table[j-1][i+(1<<(j-1))])
        self.log=[0]*(self.n+1)
        for i in range(2,self.n+1): self.log[i]=self.log[i//2]+1
    def query(self, l, r):
        j=self.log[r-l+1]
        return self.fn(self.table[j][l],self.table[j][r-(1<<j)+1])

if __name__=="__main__":
    arr=[1,3,2,7,9,11,3,5,6,2,8]
    st_min=SparseTable(arr,min); st_max=SparseTable(arr,max)
    print(f"Array: {arr}")
    queries=[(0,3),(2,6),(4,10),(0,10)]
    for l,r in queries:
        print(f"  [{l}..{r}]: min={st_min.query(l,r)}, max={st_max.query(l,r)}")

#!/usr/bin/env python3
"""Sparse table for O(1) range minimum queries."""
import sys,math
class SparseTable:
    def __init__(self,arr):
        n=len(arr); k=int(math.log2(n))+1 if n else 0
        self.table=[[0]*n for _ in range(k)]
        self.log=[0]*(n+1)
        for i in range(2,n+1): self.log[i]=self.log[i//2]+1
        self.table[0]=list(arr)
        for j in range(1,k):
            for i in range(n-(1<<j)+1):
                self.table[j][i]=min(self.table[j-1][i],self.table[j-1][i+(1<<(j-1))])
    def query(self,l,r):
        k=self.log[r-l+1]
        return min(self.table[k][l],self.table[k][r-(1<<k)+1])
def main():
    arr=[7,2,3,0,5,10,3,12,18,1]
    st=SparseTable(arr)
    print(f"Array: {arr}")
    queries=[(0,4),(2,7),(0,9),(5,8)]
    for l,r in queries:
        print(f"  min[{l}..{r}] = {st.query(l,r)}")
if __name__=="__main__": main()

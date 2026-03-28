#!/usr/bin/env python3
"""sparse_table - O(1) range minimum/maximum queries."""
import sys,math
class SparseTable:
    def __init__(s,data,fn=min):
        s.fn=fn;n=len(data);s.k=int(math.log2(n))+1 if n else 0
        s.table=[[0]*n for _ in range(s.k)];s.table[0]=list(data);s.log=[0]*(n+1)
        for i in range(2,n+1):s.log[i]=s.log[i//2]+1
        for j in range(1,s.k):
            for i in range(n-(1<<j)+1):s.table[j][i]=fn(s.table[j-1][i],s.table[j-1][i+(1<<(j-1))])
    def query(s,l,r):
        j=s.log[r-l+1];return s.fn(s.table[j][l],s.table[j][r-(1<<j)+1])
if __name__=="__main__":
    data=[1,3,2,7,9,11,3,5,6,4,8];st=SparseTable(data);print(f"Data: {data}")
    queries=[(0,4),(2,7),(5,10),(0,10),(3,3)]
    for l,r in queries:print(f"  min[{l}..{r}] = {st.query(l,r)}")
    stmax=SparseTable(data,max);print("Max queries:")
    for l,r in queries:print(f"  max[{l}..{r}] = {stmax.query(l,r)}")

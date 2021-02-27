from typing import *
class Unionfind:
    def  __init__(self,n) -> None:
        """[summary]
        Args:
            n (int): number of node
        """
        self.parent=[i for i in range(n)]
        self.weight=[0 for i in range(n)]
    def union(self,p: int,q: int) -> None:
        pRoot,qRoot=self.find(p),self.find(q)
        if pRoot==qRoot: return
        # weighted union making the tree balance
        if self.weight[pRoot]<self.weight[qRoot]:
            self.parent[pRoot]=qRoot
        elif self.weight[pRoot]>self.weight[qRoot]:
            self.parent[qRoot]=pRoot
        else:
            self.parent[qRoot]=pRoot
            self.weight[pRoot]+=1
    def find(self,p: int) -> int:
        pRoot=p
        while(pRoot!=self.parent[pRoot]):
            pRoot=self.parent[pRoot]
        # Path Compression: move the node from child of parent to child of root
        while (p!=self.parent[p]): 
            tmp=self.parent[p]
            self.parent[p]=pRoot
            p=tmp
        return pRoot
    def connected(self,p: int,q: int)-> bool:
        return self.find(p)==self.find(q)

if __name__=='__main__':
    un=Unionfind(10)
    un.union(0,1)
    un.union(1,2)
    un.union(4,5)
    un.union(3,4)
    un.union(1,4)
    un.union(3,6)
    un.union(2,3)
    un.union(7,8)
    un.union(5,7)
    print(un.weight,un.parent)

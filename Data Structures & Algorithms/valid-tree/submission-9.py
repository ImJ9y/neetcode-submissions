class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False

        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(n):
            res = n
            while parents[res] != res:
                parents[res] = parents[parents[res]]
                res = parents[res]
            
            return res
        
        def union(n1, n2):
            u1, u2 = find(n1), find(n2)

            if u1 == u2:
                return False
            
            if u1 < u2:
                parents[u1] = u2
                ranks[u2] += ranks[u1]
            else:
                parents[u2] = u1
                ranks[u1] += ranks[u2]
            
            return True
        

        for e, v in edges:
            if not(union(e, v)):
                return False
        
        return True
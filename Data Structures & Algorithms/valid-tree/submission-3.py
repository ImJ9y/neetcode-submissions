class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != parents[res]:
                parents[res] = parents[parents[res]]
                res = parents[res]
            
            return res

        def union(n1, n2):
            u1, u2 = find(n1), find(n2)

            if u1 == u2:
                return False
            
            if u1 < u2:
                parents[u1] = u2
                rank[u2] += rank[u1]
            else:
                parents[u2] = u1
                rank[u1] += rank[u2]
            
            return True
        
        for n1, n2 in edges:
            if not(union(n1,n2)):
                return False
        
        return True
        
            

class Solution:
    def isMonotonic(self, A) -> bool:
        a=sorted(A)
        b=sorted(A,reverse=True)
        if (a == A):
            return True
        if (b == A):
            return True
        else:
            return False
s=Solution()
lst=[1,2,2,3]
print(s.isMonotonic(lst))            
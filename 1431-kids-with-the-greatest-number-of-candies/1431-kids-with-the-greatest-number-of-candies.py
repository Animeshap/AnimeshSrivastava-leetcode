class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=0
        for candy in candies:
            maximum=max(maximum,candy)
            
        res=[]
        for i in range(len(candies)):
            candies[i]+=extraCandies
            if candies[i]>=maximum:
                res.append(True) 
            else:
                res.append(False) 
        return res
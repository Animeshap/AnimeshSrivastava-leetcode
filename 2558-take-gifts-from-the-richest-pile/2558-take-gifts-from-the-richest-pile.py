class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0]= int(gifts[0]**0.5)
        count=0
        for gift in gifts:
            count+=gift
        return count





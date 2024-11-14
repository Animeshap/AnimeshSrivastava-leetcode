class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total=0
        for stone in stones:
            for jewel in jewels:
                if stone==jewel:
                    total+=1
        return total
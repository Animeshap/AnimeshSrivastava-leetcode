class Solution:
    def isBalanced(self, num: str) -> bool:
        eventotal=0
        oddtotal=0
        for i in range(len(num)):
            if i%2==0:
                eventotal+=int(num[i])
            else:
                oddtotal+=int(num[i])
        return eventotal==oddtotal
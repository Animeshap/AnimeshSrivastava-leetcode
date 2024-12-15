class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans=events[0][0]
        max_time=events[0][1]
        for i in range(1,len(events)):
            time=events[i][1]-events[i-1][1]
            if time>max_time:
                max_time=time
                ans=events[i][0]
            elif time==max_time:
                ans=min(ans,events[i][0])
        return ans
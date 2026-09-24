class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low=0
        high=1
        count={}
        max_length=0

        for high in range (len(s)):
            count[s[high]]=count.get(s[high],0)+1

            while (count[s[high]]>1):
                count[s[low]]-=1
                low+=1

            max_length=max(max_length,high-low+1)
        return max_length
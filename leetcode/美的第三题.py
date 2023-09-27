class Solution:
    def check_is_youya(self,sub):
        n=len(sub)
        for i in range(n):
            for j in range(i+1,n):
                if sub[i] & sub[j] !=0:
                    return False
        return True

    def longestNiceSubarray(self , nums) -> int:
        # write code here
        n=len(nums)
        max_len=1
        for i in range(n):
            for j in range(i+2,n+1):
                sub=nums[i:j]
                if self.check_is_youya(sub):
                    max_len=max(max_len,j-i)
        return max_len

s=Solution()
max_len=s.longestNiceSubarray([3,1,5,11,13])
print(max_len)
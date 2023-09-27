class Solution:
    def canPlaceTrees(self, woodland, n: int):
        # write code here
        count = 0
        if woodland[0] == 0 and woodland[1] == 0:
            count += 1
            woodland[0] = 1
        woodland_tmp=[_/2 for _ in woodland]
        before_wood=[0]+woodland_tmp[:-1]
        after_wood=woodland_tmp[1:]+[0]
        sum_add=[woodland[i]-before_wood[i]-after_wood[i] for i in range(len(woodland))]
        print(sum_add)

        count_tmp=0
        state=0
        for i in range(len(woodland)):
            if state==0 and woodland[i]-before_wood[i]-after_wood[i]==-0.5:
                state=1
            elif state in [1,2] and woodland[i]-before_wood[i]-after_wood[i]==0:
                state=2
                count_tmp+=1
            elif state==2 and woodland[i]-before_wood[i]-after_wood[i]==-0.5:
                state=0
                count+=((count_tmp+1)//2)
            else:
                state=0
                count_tmp=0

        return count>=n


s=Solution()
c=s.canPlaceTrees([0,0,0,0,0,1,0],2)
print(c)
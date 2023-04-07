"""
1124. 表现良好的最长时间段
输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
"""
class Solution:
    def longestWPI(self, hours) -> int:
        convertH=[]
        temp_loc=[]
        max_len=0
        for h in hours :
            if h>8 :
                convertH.append(True)
                max_len=1
            else:
                convertH.append(False)
        for i in range(len(convertH)):
            if convertH[i] :
                temp_loc.append(i)

        for loc in temp_loc:
            '''左右左生长'''
            now_sum=0
            now_len=1
            left_flag=False
            for i in range(1,loc+1):
                if convertH[loc-i]:
                    now_sum+=1
                else:
                    now_sum-=1
                if now_sum>=0:
                    now_len+=1
                elif now_sum==-1 and (loc-i-1)>=0 and convertH[loc-i-1]:
                    now_len+=1
                else:
                    now_sum+=1
                    break
            if now_len==1:
                left_flag=True


            for i in range(1,len(convertH)-loc):
                if convertH[loc+i]:
                    now_sum+=1
                else:
                    now_sum-=1
                if now_sum>=0:
                    now_len+=1
                elif now_sum==-1 and loc+i+1<len(convertH) and convertH[loc+i+1]:
                    now_len+=1
                else:
                    now_sum+=1
                    break
            if left_flag:
                for i in range(1,loc+1):
                    if convertH[loc-i]:
                        now_sum+=1
                    else:
                        now_sum-=1
                    if now_sum>=0:
                        now_len+=1
                    elif now_sum==-1 and (loc-i-1)>=0 and convertH[loc-i-1]:
                        now_len+=1
                    else:
                        now_sum+=1
                        break
            if now_len>max_len:
                max_len=now_len

        return max_len

s=Solution()
hours = [11,2,4,14,2,15,7,10,1,16,9,0,2,8,4,14,6,12,2,8,6,4,14,13,7,16,14,2,3,2,8,3,12,3,3,9,14,1,5,3,12,0,15,5,0,2,3,16,7,2,1,1,4,9,0,11,9,16,15,7,0,5,6,4,12,1,1,2,13,8,3,9,12,9,3,11,4,14,7,5,16,0,11,8,8,14,1,5,0,6,5,8,10,15,9,14,16,11,1,13]
test=s.longestWPI(hours)
print(test)
class Solution():
    def length(self,num:int)-> int:
        nowlen=0
        if num>>16==0:
            nowlen+=16
            num=num<<16
        if num>>24==0:
            nowlen+=8
            num=num<<8
        if num>>28==0:
            nowlen+=4
            num=num<<4
        if num>>30==0:
            nowlen+=2
            num=num<<2
        if num>>31==0:
            nowlen+=1

        nowlen=32-nowlen
        return nowlen

    def count(self,num:int)-> int:
        num=(num & 0x55555555) + ((num>>1) & 0x55555555) #每两个格子为一个独立，每个独立表述原来相邻的1个数和
        num=(num & 0x33333333) + ((num>>2) & 0x33333333) #相邻的两小块相加
        num=(num & 0x0F0F0F0F) + ((num>>4) & 0x0F0F0F0F) #相邻的四小块相加
        num=(num & 0x00FF00FF) + ((num>>8) & 0x00FF00FF) #相邻的八小块相加
        num=(num & 0x0000FFFF) + ((num>>16)& 0x0000FFFF) #相邻的16小块相加
        return num

    def numberOfSteps(self, num: int) -> int:
        #将相邻的奇数和偶数合并到到[/2]这一步，即先判断奇偶，奇数多加一步
        ans=0
        while num:
            ans+=ans&1
            if num>1:
                ans+=1
            num=num//2
        return ans

    def numberOfSteps2(self,num:int)->int:
        return self.length(num)-1+self.count(num)


a=14
s=Solution()
b=s.numberOfSteps2(a)

print(b)
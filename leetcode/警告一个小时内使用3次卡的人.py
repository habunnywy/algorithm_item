class Solution:
    def alertNames(self, keyName, keyTime):
        Namedict=dict()
        for i in range(len(keyName)):
            if keyName[i] not in Namedict.keys():
                Namedict[keyName[i]]=[keyTime[i]]
            else:
                Namedict[keyName[i]].append(keyTime[i])
        alertList=[]
        for name,timeList in Namedict.items():
            temp_time=[t.split(':') for t in timeList]
            temp_time=[int(t[0])*60+int(t[1]) for t in temp_time]
            temp_time.sort()
            dec_time=[temp_time[st+2]-temp_time[st]for st in range(len(temp_time[:-2]))]
            for temp in dec_time:
                if temp<=60 and temp>=0:
                    alertList.append(name)
                    break
        alertList.sort()
        return alertList

s=Solution()
keyName=["a","a","a","a","a","b","b","b","b","b","b"]
keyTime=["04:48","23:53","06:36","07:45","12:16","00:52","10:59","17:16","00:36","01:26","22:42"]

out=s.alertNames(keyName,keyTime)
print(out)

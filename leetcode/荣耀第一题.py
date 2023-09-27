first_line=input().strip()
second_line=input().strip()
# 去除first_line中的空格
first_line=first_line.replace(' ','')
# 去除first_line中的tap
first_line=first_line.replace('\t','')
count=0
first_pointer=0
second_pointer=0
for i in range(len(first_line)):
    if first_line[i]==second_line[0]:
        for j in range(len(second_line)):
            if (i+j)<len(first_line) and first_line[i+j]==second_line[j]:
                if j==len(second_line)-1:
                    count+=1
                continue
            else:
                break

print(count)

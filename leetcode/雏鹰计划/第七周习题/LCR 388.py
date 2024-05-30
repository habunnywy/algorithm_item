'''
假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例：

这里将 dir 作为根目录中的唯一目录。dir 包含两个子目录 subdir1 和 subdir2 。
subdir1 包含文件 file1.ext 和子目录 subsubdir1；subdir2 包含子目录 subsubdir2，该子目录下包含文件 file2.ext 。
'''

class Solution:

    def lengthLongestPath(self, input: str) -> int:
        if '.' not in input:
            return 0

        max_len = 0
        i,n = 0,len(input)
        folder_len_list = [] # 当前遍历到的文件的每一级父路径的长度
        while i < n:
            # 根据文件前面的\t数量去判断文件的深度
            depth = 1
            while input[i] == '\t':
                depth += 1
                i += 1

            is_File = False
            tmp_len = 0
            while i < n and input[i] != '\n': # 统计加下了一级的文件or文件夹长度
                if input[i]=='.':
                    is_File = True
                tmp_len += 1
                i += 1
            else:
                i += 1 #因为碰到'\n'了，跳过

            # 把前面的长度所有父路劲长度算上
            while len(folder_len_list) >= depth: # 如果栈中的文件夹个数大于等于当前深度，表示已经换到其它文件目录了
                folder_len_list.pop()

            # 统计当前文件|文件夹的总长度，前面还有父节点，则加父目录的长度和'\'这一长度
            if folder_len_list:
                tmp_len += folder_len_list[-1] + 1

            # 如果是文件，就直接比较长度，否则是文件夹，加入长度到栈中
            if is_File:
                max_len = max(max_len, tmp_len)
            else:
                folder_len_list.append(tmp_len)

        return max_len





if __name__ == '__main__':
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    solution = Solution()
    print(solution.lengthLongestPath(input))
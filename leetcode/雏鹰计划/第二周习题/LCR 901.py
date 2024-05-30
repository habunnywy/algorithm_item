from typing import List
'''
设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。

当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。

实现 StockSpanner 类：

StockSpanner() 初始化类对象。
int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。


示例：

输入：
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
输出：
[null, 1, 1, 1, 2, 1, 4, 6]

'''

class StockSpanner:

    def __init__(self):
        self.history_price = [float('inf')]
        self.history_max_index = [0] #记录的是第i日中最早能够比第i日价格少的日
        self.history_day = 0


    def next(self, price: int) -> int:
        self.history_price.append(price)
        self.history_day += 1

        def find_decline_day_base(end_day,start_day):
            decline_day = 0
            tmp_day = end_day
            com_price = self.history_price[end_day]
            while tmp_day>=start_day:
                if self.history_price[tmp_day]>com_price:
                    break
                decline_day += 1
                tmp_day -= 1
            return decline_day

        def find_decline_day(end_day,end_day_value):
            if end_day == 0:
                self.history_max_index.append(-1)
                return

            if end_day_value<self.history_price[end_day-1]:
                self.history_max_index.append(end_day-1)

            elif end_day_value==self.history_price[end_day-1]:
                self.history_max_index.append(self.history_max_index[end_day-1])

            else:
                upper_day = self.history_max_index[end_day-1]

                if end_day_value < self.history_price[upper_day]:
                    self.history_max_index.append(upper_day)
                elif end_day_value == self.history_price[upper_day]:
                    self.history_max_index.append(self.history_max_index[upper_day])
                else:
                    find_decline_day(upper_day,end_day_value)


        find_decline_day(self.history_day,price)
        return self.history_day - self.history_max_index[self.history_day]

class StockSpanner2:
    def __init__(self):
        self.stack = [(-1, float('inf'))]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]



if __name__ == '__main__':
    s = StockSpanner2()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(110))


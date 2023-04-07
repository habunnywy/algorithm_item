import numpy as np
class Solution:
    def maximumWealth(self, accounts) -> int:
        return max(map(sum, accounts))


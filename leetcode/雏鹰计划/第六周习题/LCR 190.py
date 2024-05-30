class Solution:
    def reverseBits(self, n: int) -> int:
        input_b = list(bin(n)[2:])
        input_b = ['0']*(32-len(input_b)) + input_b

        input_b = input_b[::-1]
        return int(''.join(input_b),2)


if __name__ == '__main__':
    n = 0b00000010100101000001111010011100
    solution = Solution()
    print(solution.reverseBits(n))
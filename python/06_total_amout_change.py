class Solution:
    def findChange(self, total_amount: int):
        result = []
        remain_amount = total_amount
        for i in [100, 50, 20, 1]:
            match i:
                case 100:
                    temp = int(remain_amount / 100)
                    result.append({"100": temp})
                    remain_amount = remain_amount - (100 * temp)
                case 50:
                    temp = int(remain_amount / 50)
                    result.append({"50": temp})
                    remain_amount = remain_amount - (50 * temp)
                case 20:
                    temp = int(remain_amount / 20)
                    result.append({"20": temp})
                    remain_amount = remain_amount - (20 * temp)
                case 1:
                    temp = int(remain_amount / 1)
                    result.append({"1": temp})
                    remain_amount = remain_amount - (1 * temp)
        
        print(result)


a = Solution().findChange(199)
        
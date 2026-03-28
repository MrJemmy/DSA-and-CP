class Solution:
    """
    670. Maximum Swap
    """

    def find_max(self, arr, search_index, max_value):
        max_index = -1
        original = True
        for i, value in enumerate(arr):
            if search_index >= i:
                continue

            if value > max_value or (value == max_value and not original):
                max_index = i
                max_value = value
                original = False
        
        return max_index

    def maximumSwap(self, num: int) -> int:
        num_copy = num
        digit_arr = []

        while num_copy != 0:
            temp = int(num_copy / 10)
            digit = num_copy - (10 * temp)
            num_copy = temp
            digit_arr.append(digit)

        digit_arr.reverse()
        
        # logic to swap
        prev = 0
        swap_index = -1
        for index, value in enumerate(digit_arr):
            if prev == value:
                continue
            
            swap_index = self.find_max(digit_arr, index, value)

            if swap_index != -1:
                print("swap_index: ", swap_index, "for index: ", index)
                print(digit_arr)
                digit_arr[index], digit_arr[swap_index] = digit_arr[swap_index], digit_arr[index]
                print(digit_arr)
                break
            
            prev = value

        digit_arr.reverse()

        result = 0
        power = 1
        for i in digit_arr:
            result = (i * power) + result
            power *= 10

        return result

print(Solution().maximumSwap(1993))

        
class Solution:
    def __init__(self, arr):
        self.arr = arr

    def swap(self):
        right_index = len(self.arr)-1 
        for left_index in range(0, int(right_index/2)):
            self.arr[left_index], self.arr[right_index] = self.arr[right_index], self.arr[left_index]
            right_index -= 1

        return self.arr


a = Solution([11, 12, 13, 14, 15])
print(a.swap())
class topInterview:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n, 1):
            nums1.pop(m)
        nums1.extend(nums2)
        nums1.sort()
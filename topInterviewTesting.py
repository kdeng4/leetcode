from topInterview import topInterview


def test_merge():
    solution = topInterview()
    nums1, m, nums2, n = [1,2,3,0,0,0], 3, [2,5,6], 3
    solution.merge(nums1, m, nums2, n)


test_merge()
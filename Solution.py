class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        prizePositions.sort()
        min_val = prizePositions[0]
        max_val = prizePositions[-1]
        if max_val - min_val <= k * 2:
            return len(prizePositions)
        else:
            range_count = {}
            for i, curr in enumerate(prizePositions):
                if curr not in range_count.keys():
                    range_count[curr] = 0
                for key in range_count.keys():
                    if key + k >= curr:
                        range_count[key] += 1  # return diction, numbers of positions in range, start position as key
            optim = 0
            while len(range_count) > 0:
                key_o = list(range_count.keys())[0]
                item_o = range_count.pop(key_o)
                total_item = 0
                for key_i, item_i in range_count.items():
                    if key_i <= key_o + k:
                        continue
                    if item_i > total_item:
                        total_item = item_i
                total_item += item_o
                if total_item > optim:
                    optim = total_item
            return optim

    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        if n < 3:
            return ans[n]
        else:
            for i in range(n - 3):
                added = sum(ans)
                ans.pop(0)
                ans.append(added)
            return sum(ans)

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for n in nums1:
            next_great = -1
            if n in nums2:
                found = None
                for idx, inner in enumerate(nums2):
                    if found is not None and inner > found:
                        next_great = inner
                        break
                    elif n == inner:
                        found = inner
            ans.append(next_great)
        return ans


    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 1
        else:
            one_step = self.climbStairs(n-1)
            two_step = self.climbStairs(n-2)
            return one_step + two_step

    def canEat(self, candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
        ans = []
        for q in queries:
            type, day, daily_cap, *_ = q
            # check i - 1 type
            last_basket = sum(candiesCount[:type])
            total_candy = candiesCount[type] + last_basket
            if (day - 1) < total_candy and day * daily_cap > last_basket and day < total_candy:
                ans.append(True)
                continue
            ans.append(False)
        return ans

    def romanToInt(self, s: str) -> int:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        intg = [1, 5, 10, 50, 100, 500, 1000]
        ans = 0

        for i in range(len(s)):
            char = s[i]
            idx = roman.index(char)
            ans += intg[idx]
        return ans

    def romanToInt(self, s: str) -> int:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        intg = [1, 5, 10, 50, 100, 500, 1000]
        num, subtol = [], []
        for i in range(len(s)):
            char = s[i]
            idx = roman.index(char)
            curr_num = intg[idx]
            if curr_num in num:
                idx = num.index(curr_num)
                subtol[idx] += curr_num
            else:
                num.append(curr_num)
                subtol.append(curr_num)
            if len(num) > 0 and curr_num > min(num):
                idx = num.index(curr_num)
                for j, curr_sub in enumerate(num):
                    if num[j] < curr_num:
                        subtol[idx] -= subtol[j]
                        num.pop(j)
                        subtol.pop(j)
                        break
        return sum(subtol)

    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if isinstance(idx, list):
            first = idx[0] + 1
        elif idx == -1:
            return word
        else:
            first = idx + 1
        seg_1_str = word[:first]
        seg_2_str = word[first:]
        seg_1_str = seg_1_str[::-1]
        return seg_1_str + seg_2_str

    def findMaxK(self, nums: list[int]) -> int:
        nums_c = nums.copy()
        while len(nums_c) > 0:
            num_max = max(nums_c)
            nums_c.remove(num_max)
            if num_max < 0:
                return -1
            elif (- num_max) in nums:
                return num_max
        return -1

    def compareVersion(self, version1: str, version2: str) -> int:
        split_1 = version1.split('.')
        split_2 = version2.split('.')
        while len(split_1) > 0 and len(split_2) > 0:
            one_temp = split_1[0]
            two_temp = split_2[0]
            split_1.remove(one_temp)
            split_2.remove(two_temp)
            one_temp = int(one_temp)
            two_temp = int(two_temp)
            if one_temp > two_temp:
                return 1
            elif one_temp < two_temp:
                return -1
        if len(split_1) == len(split_2):
            return 0

        if len(split_1) > 0:
            final = split_1
            checker = 1
        else:
            final = split_2
            checker = -1
        while len(final) > 0:
            temp = final[0]
            final.remove(temp)
            temp = int(temp)
            if temp > 0:
                return checker
        return 0


    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        boat = 0
        lower, upper = 0, len(people) - 1
        while lower <= upper:
            if (people[lower] + people[upper]) <= limit:
                lower += 1
                upper -= 1
            else:
                upper -= 1
            boat += 1
        return boat


    def longestPalindrome(self, s: str) -> str:
        ans_str, ans_num = '', 0
        center_loc = 0
        ans_left_pos = ans_right_pos = 0
        while center_loc < len(s):
            # CHECK WHEN TOTAL IS EVEN NUMBER
            left_pos, right_pos = center_loc - 1, center_loc
            left_pos, right_pos, *_ = self._longestPalindrome_expand(s, left_pos, right_pos, ans_num)
            if left_pos >= 0:
                ans_left_pos = left_pos
                ans_right_pos = right_pos
            # CHECK WHEN TOTAL IS ODD NUMBER
            left_pos, right_pos = center_loc - 1, center_loc + 1
            left_pos, right_pos, *_ = self._longestPalindrome_expand(s, left_pos, right_pos, ans_num)
            if left_pos >= 0:
                ans_left_pos = left_pos
                ans_right_pos = right_pos
            center_loc += 1
            ans_num = ans_right_pos - ans_left_pos
        ans_str = s[ans_left_pos: ans_right_pos + 1]
        return ans_str


    def _longestPalindrome_checkEqual(self, s: str, position_1: int, position_2: int) -> bool:
        if position_1 < 0 or position_2 < 0 or position_1 >= len(s) or position_2 >= len(s):
            return False
        if s[position_1] == s[position_2]:
            return True
        return False


    def _longestPalindrome_expand(self, s: str, left_pos: int, right_pos: int, max_length: int) -> (int, int):
        if left_pos < 0 or right_pos < 0 or left_pos >= len(s) or right_pos >= len(s):
            return -1, -1
        while self._longestPalindrome_checkEqual(s, left_pos, right_pos):
            left_pos -= 1
            right_pos += 1
        left_pos += 1
        right_pos -= 1
        if (right_pos - left_pos) > max_length:
            return left_pos, right_pos
        else:
            return -1, -1


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # CHECK HORIZONTAL
        for test_line in board:
            if not self._isValidSudoku_checkRec(test_line):
                return False
        # CHECK VERTICAL
        for i in range(len(board)):
            test_line = [x[i] for x in board]
            if not self._isValidSudoku_checkRec(test_line):
                return False
        # CHECK SMALL SQUARE
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                test_line = sum([x[j:j+3] for x in board[i: i+3]],[])
                if not self._isValidSudoku_checkRec(test_line):
                    return False
        return True


    def _isValidSudoku_checkRec(self, curr_list:list[str]) -> bool:
        list_to = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in list_to:
            if curr_list.count(i) > 1:
                return False
        return True

    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        for idx, curr_str in enumerate(strs):
            if len(ans) == 0:
                if idx < 1:
                    ans = curr_str
                else:
                    return ans
            else:
                while len(ans) > 0:
                    if ans in curr_str:
                        break
                    else:
                        ans = ans[:-1]
        return ans
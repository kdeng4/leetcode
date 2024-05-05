from Solution import Solution
from TestingCases import TestingCases

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def test_numRescueBoats():
    solution = Solution()
    people = TestingCases().numRescueBoats_people_1
    limit = TestingCases().numRescueBoats_limit_1
    output = solution.numRescueBoats(people, limit)
    print(output)
    return output

def test_longestPalindrome():
    solution = Solution()
    input = 'ccc'
    output = solution.longestPalindrome(input)
    print(output)


def test_isValidSudoku():
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    output = solution.isValidSudoku(board)
    print(output)


def test_validWordtest_longestCommonPrefix():
    solution = Solution()
    input = ["c","acc","ccc"]
    output = solution.longestCommonPrefix(input)
    print(output)

def test_validWord():
    sol = Solution()
    input = "234Adas"
    output = sol.isValid(input)
    print(output)

    input = "b3"
    output = sol.isValid(input)
    print(output)

    input = "a3$e"
    output = sol.isValid(input)
    print(output)


def test_minimumOperationsToMakeKPeriodic():
    s = Solution()
    word, k = "leetcodeleet", 4
    out = s.minimumOperationsToMakeKPeriodic(word, k)
    print(out)

    word, k = "leetcoleet", 2
    out = s.minimumOperationsToMakeKPeriodic(word, k)
    print(out)


def test_minAnagramLength():
    s = Solution()
    test = "cdef"
    out = s.minAnagramLength(test)
    print(f'CORRECT ANS: 4, GOTL {out}')

    test = "xxe"
    out = s.minAnagramLength(test)
    print(f'CORRECT ANS: 3, GOTL {out}')


def test_minCostToEqualizeArray():
    s = Solution()
    nums, cost1, cost2 = [2, 3, 3, 3, 5], 2, 1
    out = s.minCostToEqualizeArray(nums, cost1, cost2)
    print(f'CORRECT ANS: 6, GOT {out}')

    nums, cost1, cost2 = [4,1], 5, 2
    out = s.minCostToEqualizeArray(nums, cost1, cost2)
    print(f'CORRECT ANS: 15, GOT {out}')

    nums, cost1, cost2 = [3, 5, 3], 1, 3
    out = s.minCostToEqualizeArray(nums, cost1, cost2)
    print(f'CORRECT ANS: 4, GOT {out}')

    nums, cost1, cost2 = [1, 14, 14, 15], 2, 1
    out = s.minCostToEqualizeArray(nums, cost1, cost2)
    print(f'CORRECT ANS: 20, GOT {out}')

    nums, cost1, cost2 = [6, 10, 2], 7, 2
    out = s.minCostToEqualizeArray(nums, cost1, cost2)
    print(f'CORRECT ANS: SOMETHING, GOT {out}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_minCostToEqualizeArray()
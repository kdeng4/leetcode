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


def test_longestCommonPrefix():
    solution = Solution()
    input = ["c","acc","ccc"]
    output = solution.longestCommonPrefix(input)
    print(output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_longestCommonPrefix()
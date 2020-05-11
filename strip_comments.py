# strip_comments
"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
result = solution("apples, pears # and bananas\n
                    grapes\n
                    bananas !apples",
                    ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(string, markers):
    lines = string.split('\n')
    result = []
    for line in lines:
        result_line = line
        for marker in markers:
            i = result_line.find(marker)
            if i != -1:
                result_line = line[:i].rstrip()

        result.append(result_line)
    return '\n'.join(result)


print(solution("cherries bananas avocados bananas\noranges oranges\navocados = pears strawberries '\nbananas apples cherries watermelons apples cherries", [
      '.', '#', '=', '^', ',', '?', "'", '-', '@']))

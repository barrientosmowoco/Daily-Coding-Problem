#
# Daily Coding Problem: Problem #1 [Easy]
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#


def daily(files, goal):
    for x in files:
        y = goal - x
        if y in files:
            return True
    return False


if __name__ == "__main__":
    file = [10, 15, 3, 7]
    goal_num = 18
    print(daily(file, goal_num))

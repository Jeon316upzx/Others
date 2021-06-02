# Given a list of integers and a target integer, write a function that expresses the target
#  integer by inserting + and - operations between the list items. For example:


def findTotalWays(arr, i, k):

    # If target is reached, return 1
    if (k == 0 and i == len(arr)):
        return 1

    # If all elements are processed and
    # target is not reached, return 0
    if (i >= len(arr)):
        return 0

    # add it to target
    return (findTotalWays(arr, i + 1, k) +
            findTotalWays(arr, i + 1, k - arr[i]) +
            findTotalWays(arr, i + 1, k + arr[i]))


# In terms of time complexity, the function is in constant time O(1) but linear space because the
# function is recursive in nature and needs more space in the call stack.
# I had help from geek of geeks

from collections import Counter

def solution(A):
    needed = {val: 1 for val in set(A)}
    missing = len(needed)

    # create start and end windows for the current window
    # as well as for the result window
    cur_i = result_i = result_j = 0
    for cur_j, num in enumerate(A, 1):

        # if the location hasnt been visited before 
        # subtract from visited list
        if needed[num] > 0:
            missing -= 1
        # number of times its been visited across
        needed[num] -= 1

        # once all locations are visited at least once
        # we need to minimize the length of the window
        if not missing:
            # needed[A[cur_i]] < 0 implies that there exists
            # within our window some duplicates for A[cur_i]
            # so adjust cur_i to remove these duplicates 
            while cur_i < cur_j and needed[A[cur_i]] < 0:
                needed[A[cur_i]] += 1
                cur_i += 1

            # update the maximum length of the current window
            if not result_j or cur_j - cur_i <= result_j - result_i:
                result_i, result_j = cur_i, cur_j
    return result_j - result_i
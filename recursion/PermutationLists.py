# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
def permute(self, s):
    if len(s) == 1:
        return [s]

    perm_list = []  # resulting list
    for a in s:
        remaining_elements = [x for x in s if x != a]
        z = self.permute(remaining_elements)  # permutations of sublist
        print("A: {}".format(a))
        print("Z: {}".format(z))
        for t in z:
            perm_list.append([a] + t)

    return perm_list


def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)



def removeCharFromStr(str, index):
    endIndex = index if index == len(str) else index + 1
    return str[:index] + str[endIndex:]

# 'ab' -> a + 'b', b + 'a'
# 'abc' ->  a + bc, b + ac, c + ab
#           a + cb, b + ca, c + ba
def perm(str):
    if len(str) <= 1:
        return {str}
    permSet = set()
    for i, c in enumerate(str):
        newStr = removeCharFromStr(str, i)
        retSet = perm(newStr)
        for elem in retSet:
            permSet.add(c + elem)
    return permSet

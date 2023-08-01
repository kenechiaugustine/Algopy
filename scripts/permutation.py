from itertools import count, permutations

def allpermutations(string_input):
    total_permutation = 0
    permList = permutations(string_input)
    for perm in permList:
        total_permutation = total_permutation + 1
        print(''.join(perm))
    print('There were ' + str(total_permutation) + ' possible permutation')

if __name__ == '__main__':
    string_input = input('Enter a string: ')
    allpermutations(string_input)
